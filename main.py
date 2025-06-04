from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import shutil
import os
from facefusion_wrapper_video import swap_video_faces

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
    video_path = "temp_video.mp4"
    face_path = "temp_face.jpg"
    output_path = "output.mp4"

    with open(video_path, "wb") as f:
        shutil.copyfileobj(video.file, f)
    with open(face_path, "wb") as f:
        shutil.copyfileobj(face.file, f)

    swap_video_faces(video_path, face_path, output_path, resolution)

    return FileResponse(output_path, media_type="video/mp4", filename="result.mp4")
