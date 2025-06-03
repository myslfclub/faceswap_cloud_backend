
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import base64
from facefusion_wrapper import run_facefusion

app = FastAPI()

@app.post("/faceswap")
async def faceswap(source: UploadFile = File(...), target: UploadFile = File(...)):
    with open("input_video.mp4", "wb") as f:
        shutil.copyfileobj(source.file, f)
    with open("input_face.jpg", "wb") as f:
        shutil.copyfileobj(target.file, f)

    output_path = run_facefusion("input_video.mp4", "input_face.jpg")

    with open(output_path, "rb") as vid_file:
        encoded = base64.b64encode(vid_file.read()).decode("utf-8")
    return JSONResponse(content={"result_base64": encoded})
