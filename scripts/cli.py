import argparse, os
from insightface.app import FaceAnalysis
from insightface.utils import face_align
import cv2

def face_swap(source_path, target_path, output_path):
    app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
    app.prepare(ctx_id=0)

    source_img = cv2.imread(source_path)
    target_video = cv2.VideoCapture(target_path)

    faces = app.get(source_img)
    if not faces:
        raise ValueError("No face detected in source image")
    source_face = faces[0]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = target_video.get(cv2.CAP_PROP_FPS)
    width = int(target_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(target_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = target_video.read()
        if not ret:
            break
        out.write(frame)

    target_video.release()
    out.release()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', required=True)
    parser.add_argument('--source', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--execution-provider', default="cpu")
    args = parser.parse_args()

    face_swap(args.source, args.target, args.output)
