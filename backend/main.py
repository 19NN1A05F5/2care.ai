from fastapi import FastAPI
from agent.ai_agent import process_request
from services.speech_to_text import speech_to_text
from services.text_to_speech import text_to_speech

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/voice")
def voice_agent(audio_input: str):

    text = speech_to_text(audio_input)

    response = process_request(text)

    audio = text_to_speech(response)

    return {
        "text_response": response,
        "audio_response": audio
    }
