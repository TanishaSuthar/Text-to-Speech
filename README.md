# 🗣️ Text-to-Speech Translation API (English ↔ Hindi)

A FastAPI-based web application that allows users to:
- Translate text between **English and Hindi**
- Convert the translated text into **speech (MP3 audio)**
- Download the generated audio file

---

## 🚀 Features

- 🌐 Translate text between English and Hindi
- 🔊 Generate audio from translated text using Google Text-to-Speech
- 📥 Download MP3 audio files
- ⚡ Built with FastAPI for high performance and easy documentation via Swagger UI

---

## 🧰 Technologies Used

| Technology     | Purpose                                |
|----------------|-----------------------------------------|
| Python         | Core programming language               |
| FastAPI        | Web framework for API development       |
| Uvicorn        | ASGI server to run FastAPI apps         |
| googletrans    | Language translation                    |
| gTTS (Google TTS) | Text-to-Speech conversion            |

---

## 📁 Project Structure
text-to-speech-api/
├── main.py # Main FastAPI application
├── static/ # Folder to store generated audio files (auto-created)


