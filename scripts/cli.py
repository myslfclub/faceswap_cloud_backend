import argparse, os, cv2
from insightface.app import FaceAnalysis
from insightface.utils import face_align
import numpy as np

def face_swap(source_path, target_path, output_path):
    app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
    app.prepare(ctx_id=0)

    source_img = cv2.imread(source_path)
    source_faces = app.get(source_img)
    if not source_faces:
        raise ValueError("No face detected in source image.")
    source_face = source_faces[0]
    source_embedding = source_face.embedding

    cap = cv2.VideoCapture(target_path)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = app.get(frame)
        for face in faces:
            x1, y1, x2, y2 = face.bbox.astype(int)
            if (x2 - x1) < 20 or (y2 - y1) < 20:
                continue

            sim = np.dot(face.embedding, source_embedding) / (
                np.linalg.norm(face.embedding) * np.linalg.norm(source_embedding)
            )
            if sim > 0.85:
                continue

            aligned_face = face_align.norm_crop(source_img, source_face.kps)
            frame[y1:y2, x1:x2] = cv2.resize(aligned_face, (x2 - x1, y2 - y1))

        out.write(frame)

    cap.release()
    out.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--execution-provider", default="cpu")
    args = parser.parse_args()

    face_swap(args.source, args.target, args.output)
