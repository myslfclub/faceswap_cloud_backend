from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import uuid
import os
from app.faceswap import run_faceswap

app = FastAPI()

@app.post("/faceswap")
async def faceswap(source: UploadFile = File(...), target: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    source_path = f"temp/source_{uuid.uuid4().hex}.jpg"
    target_path = f"temp/target_{uuid.uuid4().hex}.jpg"
    result_path = f"temp/result_{uuid.uuid4().hex}.jpg"

    with open(source_path, "wb") as buffer:
        shutil.copyfileobj(source.file, buffer)
    with open(target_path, "wb") as buffer:
        shutil.copyfileobj(target.file, buffer)

    run_faceswap(source_path, target_path, result_path)

    return FileResponse(result_path, media_type="image/jpeg")