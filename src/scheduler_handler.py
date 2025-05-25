"""
Scheduler Handler module for the Dental Agent Prototype.
This class provides a mocked interface for appointment scheduling system interactions.
"""

class SchedulerHandler:
    def __init__(self):
        print("SchedulerHandler initialized (Mock Mode).")
        self.mock_schedule = {}  # Simple in-memory storage for mock appointments

    def check_availability(self, requested_time: str) -> bool:
        print(f"SchedulerHandler (Mock): Checking availability for {requested_time}.")
        return True  # Mock always returns available

    def book_appointment(self, patient_info: dict, time_slot: str) -> str:
        print(f"SchedulerHandler (Mock): Booking appointment for {patient_info.get('name', 'Unknown')} at {time_slot}.")
        appointment_id = f"APT{len(self.mock_schedule) + 1:05d}"
        self.mock_schedule[appointment_id] = {
            "patient_info": patient_info,
            "time_slot": time_slot,
            "status": "confirmed"
        }
        return appointment_id

    def modify_appointment(self, appointment_id: str, new_time_slot: str) -> bool:
        print(f"SchedulerHandler (Mock): Modifying appointment {appointment_id} to {new_time_slot}.")
        if appointment_id in self.mock_schedule:
            self.mock_schedule[appointment_id]["time_slot"] = new_time_slot
            return True
        return False

    def cancel_appointment(self, appointment_id: str) -> bool:
        print(f"SchedulerHandler (Mock): Cancelling appointment {appointment_id}.")
        if appointment_id in self.mock_schedule:
            self.mock_schedule[appointment_id]["status"] = "cancelled"
            return True
        return False

    def get_appointment_details(self, appointment_id: str) -> dict:
        print(f"SchedulerHandler (Mock): Fetching details for appointment {appointment_id}.")
        if appointment_id in self.mock_schedule:
            return {
                "id": appointment_id,
                "patient_name": self.mock_schedule[appointment_id]["patient_info"].get("name", "Unknown"),
                "time": self.mock_schedule[appointment_id]["time_slot"],
                "status": self.mock_schedule[appointment_id]["status"]
            }
        return {"id": appointment_id, "patient_name": "Unknown", "time": "Unknown", "status": "not_found"} 