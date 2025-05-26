from google_calendar_handler import GoogleCalendarHandler
import datetime
import pytz

def main():
    handler = GoogleCalendarHandler()

    # Use your local timezone, e.g., 'America/New_York'
    tz = pytz.timezone('America/New_York')
    now = datetime.datetime.now(tz)
    start_time = (now + datetime.timedelta(minutes=5)).replace(second=0, microsecond=0).isoformat()
    end_time = (now + datetime.timedelta(minutes=35)).replace(second=0, microsecond=0).isoformat()

    # 1. Check availability
    available = handler.check_availability(start_time, end_time)
    print(f"Availability for {start_time} to {end_time}: {available}")

    # 2. Book appointment if available
    if available:
        patient_info = {"patient_name": "Test Patient", "contact": "555-1234"}
        appt_id = handler.book_appointment(patient_info, start_time, end_time)
        print(f"Booked appointment ID: {appt_id}")

        # 3. Get appointment details
        details = handler.get_appointment_details(appt_id)
        print("Appointment details:", details)

        # 4. Modify appointment
        new_start = (now + datetime.timedelta(minutes=10)).replace(second=0, microsecond=0).isoformat()
        new_end = (now + datetime.timedelta(minutes=40)).replace(second=0, microsecond=0).isoformat()
        modified = handler.modify_appointment(appt_id, new_start, new_end)
        print(f"Modified appointment: {modified}")

        # 5. Cancel appointment
        cancelled = handler.cancel_appointment(appt_id)
        print(f"Cancelled appointment: {cancelled}")
    else:
        print("Time slot not available for booking.")

if __name__ == "__main__":
    main() 