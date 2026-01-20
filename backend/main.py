from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from tracker import analyze_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-quarter")
async def analyze_quarter(quarter: str, video: UploadFile = File(...)):
    temp_video = f"temp_{video.filename}"

    with open(temp_video, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    players = analyze_video(temp_video)
    os.remove(temp_video)

    return {
        "quarter": quarter,
        "players": players
    }
