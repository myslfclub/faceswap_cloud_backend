from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from typing import Optional
import shutil
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FaceSwap backend is running."}

@app.post("/faceswap")
async def faceswap(
    source: UploadFile = File(...),
    target: UploadFile = File(...),
    resolution: Optional[int] = Form(720)
):
    output_path = "output.mp4"
    with open("source.mp4", "wb") as buffer:
        shutil.copyfileobj(source.file, buffer)
    with open("target.jpg", "wb") as buffer:
        shutil.copyfileobj(target.file, buffer)
    # Simulation d’un traitement (à remplacer par la vraie fusion)
    shutil.copy("source.mp4", output_path)
    return FileResponse(output_path, media_type="video/mp4")