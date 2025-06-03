
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
from facefusion_wrapper import run_facefusion

app = FastAPI()

@app.post("/faceswap")
async def faceswap(source: UploadFile = File(...), target: UploadFile = File(...)):
    with open("input_video.mp4", "wb") as f:
        shutil.copyfileobj(source.file, f)
    with open("input_face.jpg", "wb") as f:
        shutil.copyfileobj(target.file, f)

    try:
        output_path = run_facefusion("input_video.mp4", "input_face.jpg")
        return FileResponse(output_path, media_type="video/mp4")
    except Exception as e:
        return {"error": str(e)}
