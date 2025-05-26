from scheduler_handler import SchedulerHandler

def main():
    # The first appointment ID from the last batch (update if needed)
    appt_id = "9p975hgvf1qnoncdesimileass"
    scheduler = SchedulerHandler()
    print(f"Cancelling appointment {appt_id}")
    success = scheduler.cancel_appointment(appt_id)
    if success:
        print("Cancellation successful!")
    else:
        print("Cancellation failed.")

if __name__ == "__main__":
    main() 