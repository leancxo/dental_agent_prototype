import pytz
import datetime
from scheduler_handler import SchedulerHandler

def main():
    # The first appointment ID from the last batch (update if needed)
    appt_id = "9p975hgvf1qnoncdesimileass"
    tz = pytz.timezone('America/New_York')
    tomorrow = datetime.datetime.now(tz).date() + datetime.timedelta(days=1)
    new_start_dt = tz.localize(datetime.datetime.combine(tomorrow, datetime.time(11, 0)))
    new_end_dt = new_start_dt + datetime.timedelta(minutes=30)
    new_start_time = new_start_dt.isoformat()
    new_end_time = new_end_dt.isoformat()

    scheduler = SchedulerHandler()
    print(f"Modifying appointment {appt_id} to {new_start_time} - {new_end_time}")
    success = scheduler.modify_appointment(appt_id, new_start_time, new_end_time)
    if success:
        print("Modification successful!")
        details = scheduler.get_appointment_details(appt_id)
        if details and 'htmlLink' in details:
            print(f"View modified appointment: {details['htmlLink']}")
    else:
        print("Modification failed.")

if __name__ == "__main__":
    main() 