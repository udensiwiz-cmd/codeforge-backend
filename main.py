from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="CodeForge AI Studio API",
    version="1.0.0"
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

    return {
        "status": "success",
        "message": "Video request received.",
        "prompt": request.prompt,
        "style": request.style,
        "duration": request.duration,
        "ratio": request.ratio
    }
