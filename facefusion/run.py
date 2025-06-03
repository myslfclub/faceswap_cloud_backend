
import time

print("🔁 Simulating facefusion...")

time.sleep(3)  # Simulate processing

with open("output.mp4", "wb") as f:
    f.write(b"\x00" * 100000)  # Dummy binary video

print("✅ Simulated output.mp4 created.")
