from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import base64
from facefusion_wrapper import run_facefusion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/faceswap")
async def faceswap(source: UploadFile = File(...), target: UploadFile = File(...)):
    with open("input_video.mp4", "wb") as f:
        shutil.copyfileobj(source.file, f)
    with open("input_face.jpg", "wb") as f:
        shutil.copyfileobj(target.file, f)

    output_path = run_facefusion("input_video.mp4", "input_face.jpg")

    with open(output_path, "rb") as result_file:
        result_bytes = result_file.read()

    result_base64 = base64.b64encode(result_bytes).decode("utf-8")
    return {"result_base64": result_base64}
