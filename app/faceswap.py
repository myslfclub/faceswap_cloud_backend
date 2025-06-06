import subprocess

def run_faceswap(source_path, target_path, result_path):
    command = [
        "python3", "FaceFusion/main.py",
        "--source", source_path,
        "--target", target_path,
        "--output", result_path,
        "--frame-processor", "face_swapper",
        "--keep-fps", "true"
    ]
    subprocess.run(command, check=True)