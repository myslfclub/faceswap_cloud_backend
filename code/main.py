from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from facefusion_wrapper_video import swap_video_faces

app = FastAPI()

# Activer CORS si nécessaire
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/faceswap")
async def faceswap_api(
    source: UploadFile = File(...),
    target: UploadFile = File(...),
    resolution: int = Form(720)
):
    result = await swap_video_faces(source, target, resolution)
    return JSONResponse(content={"message": "Success", "result": result})
