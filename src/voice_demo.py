import os
from flask import Flask, request, Response, url_for
from twilio.twiml.voice_response import VoiceResponse
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Config
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

@app.route("/voice", methods=["POST"])
def voice():
    """Handle incoming call: prompt for a message and record it."""
    resp = VoiceResponse()
    resp.say("Hello! Please leave a message after the beep. Press any key when done.", voice='alice')
    resp.record(
        action=url_for('recording', _external=True),
        max_length=30,
        finish_on_key="#"
    )
    resp.say("We did not receive a recording. Goodbye!", voice='alice')
    return Response(str(resp), mimetype='text/xml')

@app.route("/recording", methods=["POST"])
def recording():
    """Handle the recording callback: send to ElevenLabs for transcription and play back a response."""
    recording_url = request.form.get("RecordingUrl")
    caller = request.form.get("From")
    print(f"Received recording from {caller}: {recording_url}")
    transcript = transcribe_with_elevenlabs(recording_url)
    print(f"Transcript: {transcript}")
    resp = VoiceResponse()
    if transcript:
        resp.say(f"You said: {transcript}", voice='alice')
    else:
        resp.say("Sorry, we could not transcribe your message.", voice='alice')
    resp.hangup()
    return Response(str(resp), mimetype='text/xml')

def transcribe_with_elevenlabs(recording_url):
    """Download the recording and send to ElevenLabs for transcription."""
    if not ELEVENLABS_API_KEY:
        print("No ElevenLabs API key set. Returning mock transcript.")
        return "This is a mock transcript."
    try:
        # Download the audio file from Twilio
        audio_response = requests.get(f"{recording_url}.wav")
        audio_response.raise_for_status()
        audio_data = audio_response.content
        # Send to ElevenLabs API (replace with actual endpoint and headers)
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
        }
        files = {
            "audio": ("audio.wav", audio_data, "audio/wav")
        }
        # Placeholder endpoint for ElevenLabs STT (replace with actual endpoint)
        stt_url = "https://api.elevenlabs.io/v1/speech-to-text"
        response = requests.post(stt_url, headers=headers, files=files)
        if response.status_code == 200:
            return response.json().get("text", "")
        else:
            print(f"ElevenLabs STT error: {response.text}")
            return None
    except Exception as e:
        print(f"Error in ElevenLabs transcription: {e}")
        return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 