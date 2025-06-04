from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import base64

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "✅ FaceSwap API is running!"})

@app.post("/faceswap")
async def faceswap(source: UploadFile = File(...), target: UploadFile = File(...)):
    # Simulation du résultat
    with open("output.mp4", "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    return {"result_base64": encoded_string}
