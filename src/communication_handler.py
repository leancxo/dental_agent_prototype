"""
Communication Handler module for the Dental Agent Prototype.
This class provides a mocked interface for all communication channels (SMS, voice calls), and real email via SendGrid if configured.
"""

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class CommunicationHandler:
    def __init__(self):
        print("CommunicationHandler initialized (Mock Mode).")
        self.sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
        self.email_from = os.getenv("EMAIL_FROM")
        self.email_to = os.getenv("EMAIL_TO")  # Optional, can be set per message

    def receive_inbound_message(self, source_contact: str, message_body: str) -> dict:
        print(f"CommunicationHandler (Mock): Received message from {source_contact}: '{message_body}'")
        return {
            "contact": source_contact,
            "message": message_body,
            "type": "SMS"
        }

    def send_outbound_message(self, target_contact: str, message_body: str, channel: str = "SMS") -> bool:
        if channel.upper() == "EMAIL" and self.sendgrid_api_key and self.email_from:
            return self.send_email(target_contact, message_body)
        print(f"CommunicationHandler (Mock): Sending {channel} to {target_contact}: '{message_body}'")
        return True

    def send_email(self, target_email: str, message_body: str) -> bool:
        if not self.sendgrid_api_key or not self.email_from:
            print("SendGrid not configured. Falling back to mock email.")
            print(f"Mock Email to {target_email}: {message_body}")
            return True
        try:
            message = Mail(
                from_email=self.email_from,
                to_emails=target_email or self.email_to,
                subject="Dental Agent Follow-up",
                plain_text_content=message_body
            )
            sg = SendGridAPIClient(self.sendgrid_api_key)
            response = sg.send(message)
            print(f"SendGrid Email sent to {target_email or self.email_to}. Status: {response.status_code}")
            return response.status_code < 300
        except Exception as e:
            print(f"Error sending email via SendGrid: {e}")
            return False

    def initiate_outbound_call_simulation(self, target_contact: str, call_script_identifier: str) -> str:
        print(f"CommunicationHandler (Mock): Simulating outbound call to {target_contact} using script '{call_script_identifier}'.")
        return "call_sim_id_789"

    def handle_inbound_call_simulation(self, caller_id: str) -> dict:
        print(f"CommunicationHandler (Mock): Simulating inbound call from {caller_id}.")
        return {
            "caller_id": caller_id,
            "initial_utterance": "Hello, I'd like to make an appointment."
        } 