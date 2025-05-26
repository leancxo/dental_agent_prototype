"""
Scheduler Handler module for the Dental Agent Prototype.
This class provides a mocked interface for appointment scheduling system interactions.
"""

import os
from typing import Dict

SCHEDULER_PROVIDER = os.getenv("SCHEDULER_PROVIDER", "mock").lower()

if SCHEDULER_PROVIDER == "google":
    from google_calendar_handler import GoogleCalendarHandler

class SchedulerHandler:
    def __init__(self):
        if SCHEDULER_PROVIDER == "google":
            self.google_handler = GoogleCalendarHandler()
            print("SchedulerHandler using Google Calendar integration.")
        else:
            print("SchedulerHandler initialized (Mock Mode).")
            self.mock_schedule = {}  # Simple in-memory storage for mock appointments

    def check_availability(self, requested_time: str, end_time: str = None) -> bool:
        if SCHEDULER_PROVIDER == "google":
            # For Google, requested_time and end_time must be ISO8601 strings
            if not end_time:
                raise ValueError("end_time is required for Google Calendar scheduling.")
            return self.google_handler.check_availability(requested_time, end_time)
        print(f"SchedulerHandler (Mock): Checking availability for {requested_time}.")
        return True  # Mock always returns available

    def book_appointment(self, patient_info: dict, time_slot: str, end_time: str = None) -> str:
        if SCHEDULER_PROVIDER == "google":
            if not end_time:
                raise ValueError("end_time is required for Google Calendar scheduling.")
            return self.google_handler.book_appointment(patient_info, time_slot, end_time)
        print(f"SchedulerHandler (Mock): Booking appointment for {patient_info.get('name', 'Unknown')} at {time_slot}.")
        appointment_id = f"APT{len(self.mock_schedule) + 1:05d}"
        self.mock_schedule[appointment_id] = {
            "patient_info": patient_info,
            "time_slot": time_slot,
            "status": "confirmed"
        }
        return appointment_id

    def modify_appointment(self, appointment_id: str, new_time_slot: str, new_end_time: str = None) -> bool:
        if SCHEDULER_PROVIDER == "google":
            if not new_end_time:
                raise ValueError("new_end_time is required for Google Calendar scheduling.")
            return self.google_handler.modify_appointment(appointment_id, new_time_slot, new_end_time)
        print(f"SchedulerHandler (Mock): Modifying appointment {appointment_id} to {new_time_slot}.")
        if appointment_id in self.mock_schedule:
            self.mock_schedule[appointment_id]["time_slot"] = new_time_slot
            return True
        return False

    def cancel_appointment(self, appointment_id: str) -> bool:
        if SCHEDULER_PROVIDER == "google":
            return self.google_handler.cancel_appointment(appointment_id)
        print(f"SchedulerHandler (Mock): Cancelling appointment {appointment_id}.")
        if appointment_id in self.mock_schedule:
            self.mock_schedule[appointment_id]["status"] = "cancelled"
            return True
        return False

    def get_appointment_details(self, appointment_id: str) -> dict:
        if SCHEDULER_PROVIDER == "google":
            return self.google_handler.get_appointment_details(appointment_id)
        print(f"SchedulerHandler (Mock): Fetching details for appointment {appointment_id}.")
        if appointment_id in self.mock_schedule:
            return {
                "id": appointment_id,
                "patient_name": self.mock_schedule[appointment_id]["patient_info"].get("name", "Unknown"),
                "time": self.mock_schedule[appointment_id]["time_slot"],
                "status": self.mock_schedule[appointment_id]["status"]
            }
        return {"id": appointment_id, "patient_name": "Unknown", "time": "Unknown", "status": "not_found"} 