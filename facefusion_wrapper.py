
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
    print("▶️ STDOUT:", result.stdout)
    print("⚠️ STDERR:", result.stderr)
    if result.returncode != 0:
        raise RuntimeError(f"FaceFusion failed: {result.stderr}")
    return output_path
