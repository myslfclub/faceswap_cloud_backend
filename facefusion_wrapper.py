import shutil

def run_facefusion(video_path, face_path):
    # Simulation d'une sortie valide (dans un cas réel, ici serait appelé un subprocess)
    shutil.copy("test_data/output.mp4", "result.mp4")
    return "result.mp4"
