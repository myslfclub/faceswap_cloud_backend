
import subprocess

def run_facefusion(source_path: str, target_path: str) -> str:
    output_path = "output.jpg"
    command = [
        "python", "run.py",
        "--source", source_path,
        "--target", target_path,
        "--output", output_path,
        "--keep-frames", "false"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FaceFusion failed: {result.stderr}")
    return output_path
