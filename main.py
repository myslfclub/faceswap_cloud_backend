from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

@app.post("/faceswap")
async def faceswap(source: UploadFile = File(...), target: UploadFile = File(...), resolution: str = Form(...)):
    with open("source.mp4", "wb") as s:
        s.write(await source.read())
    with open("target.jpg", "wb") as t:
        t.write(await target.read())
    # Simule une vidéo de sortie (à remplacer par appel à FaceFusion)
    with open("output.mp4", "wb") as out:
        out.write(b"FAKE MP4 CONTENT")
    return FileResponse("output.mp4", media_type="video/mp4")