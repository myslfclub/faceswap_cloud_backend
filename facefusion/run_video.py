
import sys
import subprocess

def parse_args():
    args = sys.argv
    params = {
        "source": "",
        "target": "",
        "output": "output.mp4"
    }
    if "--source" in args:
        params["source"] = args[args.index("--source") + 1]
    if "--target" in args:
        params["target"] = args[args.index("--target") + 1]
    if "--output" in args:
        params["output"] = args[args.index("--output") + 1]
    return params

def run_facefusion(params):
    command = [
        "python", "run.py",
        "--source", params["source"],
        "--target", params["target"],
        "--output", params["output"],
        "--keep-frames", "false"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError("FaceFusion execution failed.")

if __name__ == "__main__":
    params = parse_args()
    run_facefusion(params)
