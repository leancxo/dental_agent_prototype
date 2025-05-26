"""
Google Calendar Handler for Dental Agent Prototype

This handler integrates with Google Calendar API to manage real appointments.

Setup:
- Go to https://console.cloud.google.com/
- Create a project, enable Google Calendar API
- Create OAuth 2.0 credentials (Desktop App)
- Download credentials.json and place it in the project root (NOT in src/)
- First run will prompt for Google login and store token.json (do not commit these files)

Dependencies:
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""

import datetime
import os.path
from typing import Dict, Optional
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/calendar']

class GoogleCalendarHandler:
    def __init__(self, calendar_id: str = 'primary'):
        self.creds = None
        self.calendar_id = calendar_id
        self.service = self._authenticate()
        print(f"GoogleCalendarHandler initialized for calendar: {calendar_id}")

    def _authenticate(self):
        """Authenticate and return the Google Calendar service object."""
        if os.path.exists('../token.json'):
            self.creds = Credentials.from_authorized_user_file('../token.json', SCOPES)
        # If there are no (valid) credentials, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('../credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=8080)
            # Save the credentials for the next run
            with open('../token.json', 'w') as token:
                token.write(self.creds.to_json())
        return build('calendar', 'v3', credentials=self.creds)

    def check_availability(self, start_time: str, end_time: str) -> bool:
        """Check if the time slot is available (no conflicting events)."""
        events_result = self.service.events().list(
            calendarId=self.calendar_id,
            timeMin=start_time,
            timeMax=end_time,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        return len(events) == 0

    def book_appointment(self, patient_info: Dict, start_time: str, end_time: str) -> str:
        """Book an appointment as a calendar event."""
        event = {
            'summary': f"Dental Appointment: {patient_info.get('patient_name', 'Unknown')}",
            'description': f"Patient info: {patient_info}",
            'start': {'dateTime': start_time, 'timeZone': 'America/New_York'},
            'end': {'dateTime': end_time, 'timeZone': 'America/New_York'},
        }
        created_event = self.service.events().insert(calendarId=self.calendar_id, body=event).execute()
        print(f"Booked appointment: {created_event.get('id')}")
        return created_event.get('id')

    def modify_appointment(self, appointment_id: str, new_start_time: str, new_end_time: str) -> bool:
        """Modify an existing appointment's time."""
        try:
            event = self.service.events().get(calendarId=self.calendar_id, eventId=appointment_id).execute()
            event['start']['dateTime'] = new_start_time
            event['end']['dateTime'] = new_end_time
            updated_event = self.service.events().update(calendarId=self.calendar_id, eventId=appointment_id, body=event).execute()
            print(f"Modified appointment: {appointment_id}")
            return True
        except Exception as e:
            print(f"Error modifying appointment: {e}")
            return False

    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel (delete) an appointment."""
        try:
            self.service.events().delete(calendarId=self.calendar_id, eventId=appointment_id).execute()
            print(f"Cancelled appointment: {appointment_id}")
            return True
        except Exception as e:
            print(f"Error cancelling appointment: {e}")
            return False

    def get_appointment_details(self, appointment_id: str) -> Optional[Dict]:
        """Get details for a specific appointment."""
        try:
            event = self.service.events().get(calendarId=self.calendar_id, eventId=appointment_id).execute()
            return event
        except Exception as e:
            print(f"Error fetching appointment details: {e}")
            return None 