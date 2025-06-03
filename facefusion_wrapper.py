
import facefusion.globals
from facefusion import core
from facefusion.face_analyser import get_one_face
from facefusion.typing import Face
import cv2

def run_facefusion(source_path: str, target_path: str) -> str:
    facefusion.globals.execution_providers = ['CPUExecutionProvider']
    facefusion.globals.output_path = 'output.jpg'
    facefusion.globals.face_analyser_model = 'buffalo_l'
    facefusion.globals.face_mask = True

    source_image = cv2.imread(source_path)
    target_image = cv2.imread(target_path)

    source_face: Face = get_one_face(source_image)
    target_face: Face = get_one_face(target_image)

    result_image = core.swap_face(source_face, target_face, target_image)
    cv2.imwrite(facefusion.globals.output_path, result_image)
    return facefusion.globals.output_path
