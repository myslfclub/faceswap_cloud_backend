
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import shutil, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/faceswap")
async def faceswap_endpoint(
    image: UploadFile = File(...),
    video: UploadFile = File(...),
    resolution: str = Form(...)
):
    tmp_dir = "/tmp/faceswap"
    os.makedirs(tmp_dir, exist_ok=True)

    image_path = os.path.join(tmp_dir, image.filename)
    video_path = os.path.join(tmp_dir, video.filename)

    with open(image_path, "wb") as img_file:
        shutil.copyfileobj(image.file, img_file)
    with open(video_path, "wb") as vid_file:
        shutil.copyfileobj(video.file, vid_file)

    output_path = os.path.join(tmp_dir, "result.mp4")
    shutil.copy(video_path, output_path)

    return FileResponse(output_path, media_type="video/mp4")
