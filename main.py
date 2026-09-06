from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import time


app = FastAPI(
    title="CodeForge AI Studio API",
    version="1.1.0"
)


class VideoRequest(BaseModel):
    prompt: str
    style: str
    duration: str
    ratio: str


@app.get("/")
def home():

    return {
        "status": "online",
        "message": "CodeForge AI Studio Backend is running!"
    }


@app.post("/generate-video")
def generate_video(request: VideoRequest):

    job_id = str(uuid.uuid4())

    return {
        "status": "queued",
        "job_id": job_id,
        "message": "Video generation request accepted.",
        "prompt": request.prompt,
        "style": request.style,
        "duration": request.duration,
        "ratio": request.ratio,
        "created_at": int(time.time())
    }
