
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
import shutil
import subprocess
from pathlib import Path

app = FastAPI()

@app.post("/faceswap")
async def faceswap(
    video: UploadFile = File(...),
    face: UploadFile = File(...),
    resolution: int = Form(...)
):
    # Sauvegarde des fichiers reçus
    input_video_path = Path("input_video.mp4")
    input_face_path = Path("input_face.jpg")
    output_path = Path("output.mp4")
    converted_path = Path("output_converted.mp4")

    with open(input_video_path, "wb") as f:
        shutil.copyfileobj(video.file, f)
    with open(input_face_path, "wb") as f:
        shutil.copyfileobj(face.file, f)

    # Simulation du faceswap (ici on copie l'input en output)
    shutil.copy(input_video_path, output_path)

    # Conversion avec ffmpeg
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", str(output_path),
            "-vcodec", "libx264", "-acodec", "aac",
            str(converted_path)
        ], check=True)
    except subprocess.CalledProcessError:
        return {"error": "ffmpeg failed"}

    return FileResponse(converted_path, media_type="video/mp4")
