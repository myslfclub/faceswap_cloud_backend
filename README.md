# 🧠 FaceSwap Cloud Backend (Simulé)

Ce projet est un **backend FastAPI** pour faire du FaceSwap dans le cloud.

### 🚀 Endpoints

- `POST /faceswap`  
  Prend une vidéo (`source`) et une image (`target`) et retourne une vidéo générée en base64.  
  Dans cette version de test, une vidéo noire statique est renvoyée à des fins de démonstration.

### 📦 Contenu

- `main.py` : serveur FastAPI avec l’endpoint `/faceswap`
- `facefusion_wrapper.py` : simule l’appel de FaceFusion
- `output.mp4` : exemple de vidéo de sortie simulée
- `requirements.txt` : dépendances

---

### 🔧 Démarrage local

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

### 🧪 Test avec `curl`

```bash
curl -X POST http://localhost:10000/faceswap \
  -F "source=@example.mp4" \
  -F "target=@example.jpg"
```

---

### 🌐 Déploiement Render

- Ajouter `uvicorn main:app --host 0.0.0.0 --port 10000` comme commande de lancement.
- Port attendu : `10000`

---

Projet éducatif. FaceFusion n’est pas réellement exécuté ici.