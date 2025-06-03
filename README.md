
# FaceSwap Backend with FaceFusion

## Usage
POST /faceswap with `source` and `target` images as `multipart/form-data`.
Returns a base64-encoded image.

## Example curl:
curl -X POST http://localhost:10000/faceswap \
  -F "source=@test_images/source.jpg" \
  -F "target=@test_images/target.jpg"
