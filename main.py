from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import time


app = FastAPI(
    title="CodeForge AI Studio API",
    version="1.2.0"
)


jobs = {}


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

    jobs[job_id] = {
        "status": "queued",
        "prompt": request.prompt,
        "style": request.style,
        "duration": request.duration,
        "ratio": request.ratio,
        "created_at": int(time.time())
    }

    return {
        "status": "queued",
        "job_id": job_id,
        "message": "Video generation request accepted."
    }


@app.get("/job/{job_id}")
def get_job(job_id: str):

    if job_id not in jobs:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return {
        "job_id": job_id,
        **jobs[job_id]
    }
