from scheduler_handler import SchedulerHandler
from communication_handler import CommunicationHandler
import os
from dotenv import load_dotenv

def main():
    load_dotenv()  # Ensure .env is loaded
    # The next appointment ID from the last batch (update if needed)
    appt_id = "squv67iqjj4ubhamtr5s651450"
    scheduler = SchedulerHandler()
    comm_handler = CommunicationHandler()
    print(f"Processing no-show for appointment {appt_id}")
    appt_details = scheduler.get_appointment_details(appt_id)
    print(f"Appointment details: {appt_details}")
    # Log the no-show (could increment a counter in a real system)
    print(f"No-show logged for appointment {appt_id}")
    # Send follow-up message as email
    patient_email = os.getenv("EMAIL_TO") or "test@example.com"  # Use EMAIL_TO from .env or fallback
    follow_up_message = f"We missed you for your appointment {appt_id}. Please call us to reschedule."
    comm_handler.send_outbound_message(patient_email, follow_up_message, channel="EMAIL")
    print(f"Follow-up email sent to {patient_email}: {follow_up_message}")

if __name__ == "__main__":
    main() 