from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import base64
import shutil
import os
import cv2

app = FastAPI()

@app.post("/faceswap")
async def faceswap(
    source: UploadFile = File(...),
    target: UploadFile = File(...),
    resolution: str = Form("720")
):
    try:
        # Sauvegarder les fichiers uploadés
        with open("input_video.mp4", "wb") as buffer:
            shutil.copyfileobj(source.file, buffer)
        with open("input_face.jpg", "wb") as buffer:
            shutil.copyfileobj(target.file, buffer)

        # Simulation FaceSwap : Génère une vidéo noire avec texte
        output_path = "output.mp4"
        cap = cv2.VideoCapture("input_video.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS) or 25
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.putText(frame, "Simulated FaceSwap", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            out.write(frame)
        cap.release()
        out.release()

        # Lire et encoder la vidéo générée
        with open(output_path, "rb") as f:
            video_bytes = f.read()
        encoded_result = base64.b64encode(video_bytes).decode("utf-8")

        return JSONResponse(content={"result_base64": encoded_result})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})