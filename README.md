# faceswap_cloud_backend

Backend con FastAPI para FaceSwap usando FaceFusion.

## Uso

Envía una petición POST a `/faceswap` con 2 archivos:
- `source`: imagen con la cara a insertar
- `target`: imagen objetivo

Respuesta: imagen resultante con el swap.

## Docker

```bash
docker build -t faceswap-backend .
docker run -p 8000:8000 faceswap-backend
```