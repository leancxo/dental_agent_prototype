"""
Core Dental Agent module for the Dental Agent Prototype.
This class orchestrates all the interactions between different handlers.
"""

from typing import Dict, Any

class DentalAgent:
    def __init__(self, llm_handler, scheduler_handler, comm_handler):
        self.llm_handler = llm_handler
        self.scheduler_handler = scheduler_handler
        self.comm_handler = comm_handler
        print("DentalAgent initialized with all handlers.")

    def greet_caller(self) -> str:
        message = "Hello! This is the Dental Agent prototype. How can I assist you today?"
        print(f"Agent: {message}")
        return message

    def process_inbound_communication(self, communication_input: dict):
        print(f"DentalAgent: Processing inbound communication: {communication_input}")
        user_utterance = communication_input.get('message') or communication_input.get('initial_utterance')
        intent_data = self.llm_handler.understand_intent(user_utterance)
        print(f"DentalAgent: Understood intent: {intent_data}")

        if intent_data['intent'] == 'schedule_appointment':
            self.request_schedule_appointment(intent_data.get('entities', {}))
        elif intent_data['intent'] == 'dental_question':
            self.answer_off_hours_dental_query(user_utterance)
        else:
            response = self.llm_handler.generate_text(f"Generate a polite fallback response for: {user_utterance}")
            self.comm_handler.send_outbound_message(
                communication_input.get('contact') or communication_input.get('caller_id'),
                response
            )

    def request_schedule_appointment(self, patient_details: dict):
        print(f"DentalAgent: Attempting to schedule appointment with details: {patient_details}")
        requested_time = patient_details.get('time', 'any available slot')
        is_available = self.scheduler_handler.check_availability(requested_time)

        if is_available:
            appointment_id = self.scheduler_handler.book_appointment(patient_details, requested_time)
            confirmation_message = f"Appointment confirmed for {patient_details.get('patient_name', 'you')} at {requested_time}. Your appointment ID is {appointment_id}."
            self.comm_handler.send_outbound_message(
                patient_details.get('contact_info', 'patient_contact'),
                confirmation_message
            )
        else:
            alternative_message = f"Sorry, {requested_time} is not available. Would you like to try another time?"
            self.comm_handler.send_outbound_message(
                patient_details.get('contact_info', 'patient_contact'),
                alternative_message
            )

    def request_change_appointment(self, appointment_id: str, new_time: str, patient_contact: str):
        print(f"DentalAgent: Attempting to change appointment {appointment_id} to {new_time}.")
        success = self.scheduler_handler.modify_appointment(appointment_id, new_time)
        message = f"Appointment {appointment_id} change to {new_time} {'successful' if success else 'failed'}."
        self.comm_handler.send_outbound_message(patient_contact, message)

    def request_cancel_appointment(self, appointment_id: str, patient_contact: str):
        print(f"DentalAgent: Attempting to cancel appointment {appointment_id}.")
        success = self.scheduler_handler.cancel_appointment(appointment_id)
        message = f"Appointment {appointment_id} cancellation {'successful' if success else 'failed'}."
        self.comm_handler.send_outbound_message(patient_contact, message)

    def handle_no_show_scenario(self, appointment_id: str):
        print(f"DentalAgent: Processing no-show for appointment {appointment_id}.")
        appt_details = self.scheduler_handler.get_appointment_details(appointment_id)
        follow_up_message = f"We missed you for your appointment {appointment_id} ({appt_details.get('time')}). Please call us to reschedule."
        self.comm_handler.send_outbound_message(
            appt_details.get('patient_contact', 'patient_contact_placeholder'),
            follow_up_message
        )

    def answer_off_hours_dental_query(self, query_text: str, patient_contact: str = "patient_query_contact"):
        print(f"DentalAgent: Answering off-hours query: '{query_text}'")
        answer = self.llm_handler.query_knowledge_base(query_text)
        self.comm_handler.send_outbound_message(patient_contact, answer) 