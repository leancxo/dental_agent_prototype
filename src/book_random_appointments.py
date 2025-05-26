import random
import datetime
import pytz
from scheduler_handler import SchedulerHandler

NUM_APPOINTMENTS = 10
APPT_DURATION_MINUTES = 30
START_HOUR = 9
END_HOUR = 17  # Last appointment can start at 16:30


def random_weekday_dates(num_days=7):
    tz = pytz.timezone('America/New_York')
    today = datetime.datetime.now(tz).date()
    days = []
    for i in range(num_days):
        day = today + datetime.timedelta(days=i)
        if day.weekday() < 5:  # 0=Monday, 4=Friday
            days.append(day)
    return days

def main():
    scheduler = SchedulerHandler()
    tz = pytz.timezone('America/New_York')
    days = random_weekday_dates(7)
    booked = 0
    attempts = 0
    while booked < NUM_APPOINTMENTS and attempts < NUM_APPOINTMENTS * 3:
        day = random.choice(days)
        hour = random.randint(START_HOUR, END_HOUR - 1)
        minute = random.choice([0, 30])
        start_dt = tz.localize(datetime.datetime.combine(day, datetime.time(hour, minute)))
        end_dt = start_dt + datetime.timedelta(minutes=APPT_DURATION_MINUTES)
        start_time = start_dt.isoformat()
        end_time = end_dt.isoformat()
        patient_info = {"patient_name": f"Test Patient {booked+1}", "contact": f"555-00{booked+1}"}
        if scheduler.check_availability(start_time, end_time):
            appt_id = scheduler.book_appointment(patient_info, start_time, end_time)
            print(f"Booked: {patient_info['patient_name']} at {start_time} (ID: {appt_id})")
            if hasattr(scheduler, 'google_handler'):
                details = scheduler.get_appointment_details(appt_id)
                if details and 'htmlLink' in details:
                    print(f"  View: {details['htmlLink']}")
            booked += 1
        else:
            print(f"Slot not available: {start_time}")
        attempts += 1
    print(f"\nTotal appointments booked: {booked}")

if __name__ == "__main__":
    main() 