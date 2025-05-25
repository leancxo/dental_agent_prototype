"""
Main entry point for the Dental Agent Prototype.
This module provides a simulation environment to test the agent's capabilities.
"""

from llm_handler import LLMHandler
from scheduler_handler import SchedulerHandler
from communication_handler import CommunicationHandler
from agent_core import DentalAgent

def run_prototype_simulation():
    print("--- Starting Dental Agent Prototype Simulation ---")

    # Initialize handlers
    llm_handler = LLMHandler()
    scheduler_handler = SchedulerHandler()
    comm_handler = CommunicationHandler()

    # Initialize agent
    agent = DentalAgent(llm_handler, scheduler_handler, comm_handler)

    # Simulate initial greeting
    agent.greet_caller()

    # Simulate Inbound Communication for Scheduling
    print("\n--- Simulating Appointment Scheduling ---")
    mock_inbound_sms = comm_handler.receive_inbound_message(
        "123-456-7890",
        "Hi, I'd like to schedule an appointment for John Doe tomorrow at 2 PM."
    )
    agent.process_inbound_communication(mock_inbound_sms)

    # Simulate Inbound Call for Dental Question (Off-hours)
    print("\n--- Simulating Dental Question ---")
    mock_inbound_call_query = comm_handler.handle_inbound_call_simulation("987-654-3210")
    mock_inbound_call_query['message'] = "I have a bad toothache, what can I do?"
    agent.process_inbound_communication(mock_inbound_call_query)

    # Simulate a No-Show Scenario
    print("\n--- Simulating No-Show Scenario ---")
    agent.handle_no_show_scenario("APT_NOSHOW_001")

    print("\n--- Dental Agent Prototype Simulation Finished ---")

if __name__ == "__main__":
    run_prototype_simulation() 