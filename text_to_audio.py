from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import uuid

app = FastAPI()

class AudioRequest(BaseModel):
    text: str

@app.post("/generate-audio")
async def generate_audio(request: AudioRequest):
    audio_file = f"output_{uuid.uuid4().hex}.wav"
    subprocess.run(["python3", "generate_audio.py", request.text, audio_file])
    
    return {"audio_url": f"http://your-server.com/{audio_file}"}
