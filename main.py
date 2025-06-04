from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from facefusion_wrapper_video import swap_video_faces

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Backend is running"}

@app.post("/faceswap")
async def faceswap_api(
    video: UploadFile = File(...),
    face: UploadFile = File(...),
    resolution: int = Form(...)
):
    video_path = f"input_video.mp4"
    face_path = f"input_face.jpg"
    output_path = f"output.mp4"

    with open(video_path, "wb") as v:
        v.write(await video.read())
    with open(face_path, "wb") as f:
        f.write(await face.read())

    swap_video_faces(video_path, face_path, output_path, resolution)

    return FileResponse(output_path, media_type="video/mp4")
