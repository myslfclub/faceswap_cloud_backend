
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
    image: UploadFile = File(...),
    resolution: str = Form(...)
):
    # Sauvegarder les fichiers reçus
    with open("input_video.mp4", "wb") as f:
        shutil.copyfileobj(video.file, f)

    with open("input_face.jpg", "wb") as f:
        shutil.copyfileobj(image.file, f)

    # Simuler le traitement : créer une copie en sortie
    shutil.copy("input_video.mp4", "output.mp4")

    return FileResponse("output.mp4", media_type="video/mp4", filename="output.mp4")
