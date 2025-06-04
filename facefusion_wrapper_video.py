
import subprocess

def run_facefusion(source_path: str, target_path: str) -> str:
    output_path = "output.mp4"
    command = [
        "python", "run_video.py",
        "--source", source_path,
        "--target", target_path,
        "--output", output_path
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FaceFusion failed: {result.stderr}")
    return output_path
    
def swap_video_faces(source_path: str, target_path: str, output_path: str):
    # appelle ici la fonction réelle ou simule FaceFusion
    from run_video import run_facefusion_video
    run_facefusion_video(source_path, target_path, output_path)
