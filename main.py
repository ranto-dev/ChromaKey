from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from io import BytesIO
from PIL import Image
from rembg import remove # Assurez-vous d'avoir 'rembg' installé (pip install rembg)

app = FastAPI()

# Montage des fichiers statiques (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuration des templates Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Affiche la page d'accueil avec l'interface utilisateur.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/remove-bg/")
async def remove_background(file: UploadFile = File(...)):
    """
    Endpoint pour la suppression de l'arrière-plan.
    Reçoit une image, supprime le fond et renvoie l'image PNG transparente.
    """
    try:
        # Lire l'image uploadée
        image_data = await file.read()
        input_image = Image.open(BytesIO(image_data))

        # Utilisation de la fonction remove() avec des paramètres
        # pour améliorer la qualité.
        
        output_image = remove(
            input_image,
            alpha_matting=True,
            alpha_matting_foreground_threshold=240, 
            alpha_matting_background_threshold=10, 
            alpha_matting_erode_size=10, 
        )

        # Sauvegarder l'image résultante dans un buffer
        buffer = BytesIO()
        output_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Renvoyer l'image en tant que StreamingResponse
        return StreamingResponse(buffer, media_type="image/png")

    except Exception as e:
        # Gérer les erreurs de manière plus informative
        print(f"Erreur lors du traitement de l'image: {e}")
        return {"error": f"Une erreur est survenue lors du traitement de l'image: {e}"}