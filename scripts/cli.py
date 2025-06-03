import argparse
import cv2
import os
from insightface.app import FaceAnalysis

def simple_faceswap(source_img, target_frame, app):
    faces_target = app.get(target_frame)
    faces_source = app.get(source_img)

    if not faces_target or not faces_source:
        return target_frame

    x, y, w, h = faces_target[0].bbox.astype(int)
    x2, y2, w2, h2 = faces_source[0].bbox.astype(int)

    face_resized = cv2.resize(source_img[y2:h2, x2:w2], (w - x, h - y))
    target_frame[y:h, x:w] = face_resized
    return target_frame

def main(source_path, target_path, output_path):
    app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
    app.prepare(ctx_id=0)

    source_img = cv2.imread(source_path)
    video_in = cv2.VideoCapture(target_path)

    fps = video_in.get(cv2.CAP_PROP_FPS)
    width = int(video_in.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_in.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = video_in.read()
        if not ret:
            break
        swapped = simple_faceswap(source_img, frame, app)
        video_out.write(swapped)

    video_in.release()
    video_out.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    main(args.source, args.target, args.output)
