from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from googletrans import Translator
from gtts import gTTS
import uuid
import os

app = FastAPI()
translator = Translator()

@app.get("/")
def read_root():
    return {"message": "Welcome to the English-Hindi Text-to-Speech API"}

@app.get("/translate-and-speak")
def translate_and_speak(
    text: str = Query(..., description="Text to translate and convert to speech"),
    target_lang: str = Query("hi", description="Target language: 'hi' for Hindi, 'en' for English")
):
    # 🔁 Translate the text
    translated = translator.translate(text, dest=target_lang).text

    # 🗣️ Convert to speech
    tts = gTTS(translated, lang=target_lang)
    filename = f"static/audio_{uuid.uuid4().hex}.mp3"
    tts.save(filename)

    return {
        "original_text": text,
        "translated_text": translated,
        "audio_file": f"/download/{os.path.basename(filename)}"
    }

@app.get("/download/{filename}")
def download_audio(filename: str):
    file_path = f"static/{filename}"
    if os.path.exists(file_path):
        return FileResponse(path=file_path, media_type="audio/mpeg", filename=filename)
    return {"error": "File not found"}
