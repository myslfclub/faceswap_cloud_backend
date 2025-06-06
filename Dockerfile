FROM python:3.10-slim

WORKDIR /app

# Dependencias del sistema
RUN apt-get update && apt-get install -y \
    git ffmpeg libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Clonar FaceFusion
RUN git clone https://github.com/facefusion/facefusion.git FaceFusion

# Instalar dependencias de FaceFusion
RUN pip install --upgrade pip && \
    pip install -r FaceFusion/requirements.txt

# Copiar el código del backend
COPY ./app /app/app
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]