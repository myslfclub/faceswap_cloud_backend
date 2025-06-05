from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/faceswap")
async def faceswap(
    video: UploadFile = File(...),
    face: UploadFile = File(...),
    resolution: str = Form(...)
):
    with open("temp_video.mp4", "wb") as f:
        shutil.copyfileobj(video.file, f)

    with open("temp_face.jpg", "wb") as f:
        shutil.copyfileobj(face.file, f)

    return {"status": "ok", "message": "Files uploaded successfully"}
