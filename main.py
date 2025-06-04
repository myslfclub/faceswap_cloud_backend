from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/faceswap")
async def faceswap(
    video: UploadFile = File(...),
    face: UploadFile = File(...),
    resolution: int = Form(...)
):
    return {"message": "Received", "filename_video": video.filename, "filename_face": face.filename, "resolution": resolution}
