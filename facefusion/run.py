
import sys
from PIL import Image, ImageDraw

# Parse arguments (ignore them in this fake version)
# Arguments: --source input_source.jpg --target input_target.jpg --output output.jpg ...
args = sys.argv
output_file = "output.jpg"
if "--output" in args:
    output_file = args[args.index("--output") + 1]

# Create a fake result image
img = Image.new("RGB", (512, 512), color=(255, 220, 200))
draw = ImageDraw.Draw(img)
draw.text((50, 230), "FaceSwap OK", fill=(0, 0, 0))
img.save(output_file)

print(f"Simulated swap completed: {output_file}")
