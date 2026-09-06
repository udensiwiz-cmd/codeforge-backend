from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import time
import json
import os


app = FastAPI(
    title="CodeForge AI Studio API",
    version="1.3.0"
)


JOBS_FILE = "jobs.json"


class VideoRequest(BaseModel):
    prompt: str
    style: str
    duration: str
    ratio: str


def load_jobs():

    if not os.path.exists(JOBS_FILE):
        return {}

    try:

        with open(JOBS_FILE, "r") as file:
            return json.load(file)

    except Exception:

        return {}


def save_jobs(jobs):

    with open(JOBS_FILE, "w") as file:
        json.dump(jobs, file, indent=4)


@app.get("/")
def home():

    return {
        "status": "online",
        "message": "CodeForge AI Studio Backend is running!"
    }


@app.post("/generate-video")
def generate_video(request: VideoRequest):

    jobs = load_jobs()

    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "queued",
        "prompt": request.prompt,
        "style": request.style,
        "duration": request.duration,
        "ratio": request.ratio,
        "created_at": int(time.time())
    }

    save_jobs(jobs)

    return {
        "status": "queued",
        "job_id": job_id,
        "message": "Video generation request accepted."
    }


@app.get("/job/{job_id}")
def get_job(job_id: str):

    jobs = load_jobs()

    if job_id not in jobs:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return {
        "job_id": job_id,
        **jobs[job_id]
    }
