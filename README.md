# Dental Agent Prototype

A sophisticated AI assistant prototype for dental practices, designed to automate various tasks including appointment management, patient communications, and basic dental queries.

## Overview

The Dental Agent Prototype is a Python-based system that simulates an AI assistant for dental practices. It's designed with a modular architecture that allows for easy integration with real services in the future. Currently, all external system interactions (LLMs, schedulers, communication channels) are mocked for demonstration purposes.

## Features

- **Appointment Management**
  - Schedule new appointments
  - Modify existing appointments
  - Cancel appointments
  - Handle no-show scenarios
  - Send appointment reminders

- **Patient Communication**
  - Handle inbound messages and calls
  - Send outbound messages and calls
  - Process patient queries
  - Provide automated responses

- **Dental Knowledge Base**
  - Answer basic dental queries
  - Provide off-hours support
  - Access to dental care information

## Project Structure

```
dental_agent_prototype/
├── src/
│   ├── agent_core.py         # Main agent logic and orchestration
│   ├── llm_handler.py        # LLM interaction abstraction
│   ├── scheduler_handler.py  # Appointment scheduling interface
│   ├── communication_handler.py  # Communication channels interface
│   ├── config.py            # Configuration settings
│   └── main.py              # Entry point and simulation
├── .gitignore
├── requirements.txt
└── README.md
```

## Components

### DentalAgent (agent_core.py)
The main orchestrator that coordinates between different handlers and implements the core business logic.

### LLMHandler (llm_handler.py)
Interface for all Large Language Model interactions. Currently mocked, but designed to be replaced with real LLM services.

### SchedulerHandler (scheduler_handler.py)
Manages appointment scheduling operations. Currently uses in-memory storage, ready to be connected to real scheduling systems.

### CommunicationHandler (communication_handler.py)
Handles all communication channels (SMS, voice calls). Currently mocked, prepared for integration with services like Twilio.

## Getting Started

### Prerequisites
- Python 3.x
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/leancxo/dental_agent_prototype.git
cd dental_agent_prototype
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Prototype

To run the simulation:
```bash
cd src
python main.py
```

This will execute a demonstration of the agent's capabilities, including:
- Appointment scheduling
- Dental query handling
- No-show scenario management

## Development

The prototype is designed to be easily extended. To add real service integrations:

1. Replace the mock implementations in the handler classes
2. Add necessary API keys to `config.py`
3. Update `requirements.txt` with new dependencies

## Future Enhancements

- Integration with real LLM services (e.g., GPT-4, Claude)
- Connection to actual dental practice management systems
- Implementation of real communication channels (SMS, voice)
- Enhanced natural language understanding
- Advanced appointment optimization
- Patient history integration
- Analytics and reporting features

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This prototype is part of a larger initiative to modernize dental practice management
- Special thanks to all contributors and testers 