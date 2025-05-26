"""
Main entry point for the Dental Agent Prototype.
This module provides a simulation environment to test the agent's capabilities.
"""

import os
from dotenv import load_dotenv
import datetime
import pytz

from scheduler_handler import SchedulerHandler
from communication_handler import CommunicationHandler
from agent_core import DentalAgent

# Import both handlers
from llm.gpt_handler import GPTHandler
from llm.gemini_handler import GeminiHandler

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
llm_provider = os.getenv("LLM_PROVIDER", "gpt").lower()  # default to gpt

def get_llm_handler():
    if llm_provider == "gpt":
        return GPTHandler(api_key=openai_api_key)
    elif llm_provider == "gemini":
        return GeminiHandler(api_key=gemini_api_key)
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {llm_provider}")

def run_prototype_simulation():
    print(f"--- Starting Dental Agent Prototype Simulation with {llm_provider.upper()} ---")

    llm_handler = get_llm_handler()
    scheduler_handler = SchedulerHandler()
    comm_handler = CommunicationHandler()
    agent = DentalAgent(llm_handler, scheduler_handler, comm_handler)

    agent.greet_caller()

    # --- Book a real appointment you can see in your calendar ---
    print("\n--- Booking a real appointment in your Google Calendar ---")
    tz = pytz.timezone('America/New_York')
    now = datetime.datetime.now(tz)
    start_time = (now + datetime.timedelta(minutes=30)).replace(second=0, microsecond=0).isoformat()
    end_time = (now + datetime.timedelta(minutes=60)).replace(second=0, microsecond=0).isoformat()
    patient_info = {"patient_name": "Demo Patient", "contact": "555-0000"}
    available = scheduler_handler.check_availability(start_time, end_time)
    print(f"Availability for {start_time} to {end_time}: {available}")
    if available:
        appt_id = scheduler_handler.book_appointment(patient_info, start_time, end_time)
        print(f"Booked appointment ID: {appt_id}")
        # Try to print the event link if using Google Calendar
        if hasattr(scheduler_handler, 'google_handler'):
            details = scheduler_handler.get_appointment_details(appt_id)
            if details and 'htmlLink' in details:
                print(f"View your appointment in Google Calendar: {details['htmlLink']}")
    else:
        print("Time slot not available for booking.")

    print(f"\n--- Dental Agent Prototype Simulation Finished with {llm_provider.upper()} ---")

if __name__ == "__main__":
    run_prototype_simulation() 