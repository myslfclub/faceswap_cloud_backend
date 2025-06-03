
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import base64
import shutil
from facefusion_wrapper import run_facefusion

app = FastAPI()

@app.post("/faceswap")
async def faceswap(source: UploadFile = File(...), target: UploadFile = File(...)):
    with open("input_source.jpg", "wb") as f:
        shutil.copyfileobj(source.file, f)
    with open("input_target.jpg", "wb") as f:
        shutil.copyfileobj(target.file, f)

    output_path = run_facefusion("input_source.jpg", "input_target.jpg")

    with open(output_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
    return JSONResponse(content={"result_base64": encoded})
