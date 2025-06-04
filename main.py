
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
async def faceswap_api(
    video: UploadFile = File(...),
    face: UploadFile = File(...),
    resolution: str = Form(...)
):
    with open("input_video.mp4", "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
    with open("input_face.jpg", "wb") as buffer:
        shutil.copyfileobj(face.file, buffer)

    # Simulation du traitement
    shutil.copy("input_video.mp4", "output.mp4")
    return {"status": "success"}

@app.get("/faceswap")
async def read_root():
    return {"message": "FaceSwap backend is running."}

@app.get("/output")
async def get_output():
    return FileResponse("output.mp4", media_type="video/mp4")
