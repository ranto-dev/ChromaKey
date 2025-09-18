from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from io import BytesIO
from PIL import Image
from rembg import remove # Make sure to install this library

# This is a good practice to avoid errors if the templates/ or static/ directories are not found.
import os

app = FastAPI()

# Mount the static directory to serve CSS and JS files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Renders the main HTML page for the ChromaKey application.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/remove-bg/")
async def remove_background(file: UploadFile = File(...)):
    """
    API endpoint to remove the background of an uploaded image.
    """
    try:
        # Read the image data from the uploaded file
        image_data = await file.read()
        input_image = Image.open(BytesIO(image_data))

        # Use the 'rembg' library to remove the background.
        output_image = remove(input_image)

        # Save the resulting image to a BytesIO buffer
        buffer = BytesIO()
        output_image.save(buffer, format="PNG")
        buffer.seek(0)
        
        # Return the image as a StreamingResponse, which is correct for in-memory data.
        return StreamingResponse(buffer, media_type="image/png")

    except Exception as e:
        # Handle potential errors during image processing
        return {"error": str(e)}