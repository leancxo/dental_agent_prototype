# Dental Agent Prototype

A sophisticated AI assistant prototype for dental practices, designed to automate various tasks including appointment management, patient communications, and basic dental queries.

## Overview

The Dental Agent Prototype is a Python-based system that simulates an AI assistant for dental practices. It's designed with a modular architecture that allows for easy integration with real services in the future. Currently, all external system interactions (LLMs, schedulers, communication channels) are mocked for demonstration purposes, but real integrations are now available for Google Calendar, SendGrid email, and Twilio/ElevenLabs voice.

## Features

- **Appointment Management**
  - Schedule new appointments (Google Calendar integration)
  - Modify and cancel appointments
  - Handle no-show scenarios
  - Send appointment reminders

- **Patient Communication**
  - Handle inbound messages and calls
  - Send outbound messages and calls
  - Process patient queries
  - Provide automated responses
  - **Send real emails (SendGrid) and SMS (Twilio, coming soon)**
  - **Voice agent: receive phone calls, transcribe with ElevenLabs, and play back responses**

- **Dental Knowledge Base**
  - Answer basic dental queries
  - Provide off-hours support
  - Access to dental care information

## Project Structure

```
dental_agent_prototype/
├── src/
│   ├── agent_core.py         # Main agent logic and orchestration
│   ├── llm/                  # LLM handler implementations (GPT, Gemini)
│   ├── scheduler_handler.py  # Appointment scheduling interface (mock + Google Calendar)
│   ├── communication_handler.py  # Communication channels (mock, SendGrid, Twilio)
│   ├── google_calendar_handler.py # Google Calendar integration
│   ├── voice_demo.py         # Twilio + ElevenLabs voice demo (Flask app)
│   └── ...                   # Other scripts and utilities
├── .env.example
├── requirements.txt
├── README.md
```

## Voice Agent Demo (Twilio + ElevenLabs)

- **Receive a phone call via Twilio**
- **Record the caller's message**
- **Transcribe the message with ElevenLabs**
- **Play back the transcript to the caller**

### Setup
1. Set up your `.env` with Twilio and ElevenLabs credentials (see `.env.example`).
2. Run the Flask app:
   ```bash
   python3 src/voice_demo.py
   ```
3. Start ngrok:
   ```bash
   ngrok http 5000
   ```
4. Set your Twilio phone number's webhook to `https://xxxx.ngrok.io/voice`.
5. Call your Twilio number and test the flow!

## Google Calendar Integration
- Real appointment booking, modification, and cancellation using Google Calendar API.
- See your appointments in your Google Calendar in real time.

## Real Email Integration (SendGrid)
- Send real follow-up emails for no-shows or reminders.
- Configure your SendGrid API key and sender in `.env`.

## Roadmap: Conversational Voice Agent
- [ ] Multi-turn conversation: keep the call open, transcribe each utterance, and respond dynamically.
- [ ] Integrate LLM (OpenAI/Gemini) for intent detection and response generation.
- [ ] Use ElevenLabs TTS for natural voice responses.
- [ ] Full phone-based appointment management.

## Getting Started

### Prerequisites
- Python 3.x
- Git
- Twilio account and phone number
- SendGrid account
- ElevenLabs account (for voice recognition)

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

4. Copy `.env.example` to `.env` and fill in your credentials.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This prototype is part of a larger initiative to modernize dental practice management
- Special thanks to all contributors and testers 