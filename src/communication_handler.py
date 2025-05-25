"""
Communication Handler module for the Dental Agent Prototype.
This class provides a mocked interface for all communication channels (SMS, voice calls).
"""

class CommunicationHandler:
    def __init__(self):
        print("CommunicationHandler initialized (Mock Mode).")

    def receive_inbound_message(self, source_contact: str, message_body: str) -> dict:
        print(f"CommunicationHandler (Mock): Received message from {source_contact}: '{message_body}'")
        return {
            "contact": source_contact,
            "message": message_body,
            "type": "SMS"
        }

    def send_outbound_message(self, target_contact: str, message_body: str, channel: str = "SMS") -> bool:
        print(f"CommunicationHandler (Mock): Sending {channel} to {target_contact}: '{message_body}'")
        return True

    def initiate_outbound_call_simulation(self, target_contact: str, call_script_identifier: str) -> str:
        print(f"CommunicationHandler (Mock): Simulating outbound call to {target_contact} using script '{call_script_identifier}'.")
        return "call_sim_id_789"

    def handle_inbound_call_simulation(self, caller_id: str) -> dict:
        print(f"CommunicationHandler (Mock): Simulating inbound call from {caller_id}.")
        return {
            "caller_id": caller_id,
            "initial_utterance": "Hello, I'd like to make an appointment."
        } 