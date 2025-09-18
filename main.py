from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from io import BytesIO
from PIL import Image
from rembg import remove

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/remove-bg/")
async def remove_background(file: UploadFile = File(...)):
    # Read the uploaded image
    image_data = await file.read()
    input_image = Image.open(BytesIO(image_data))

    # Remove the background
    output_image = remove(input_image)

    # Save the output to a buffer
    buffer = BytesIO()
    output_image.save(buffer, format="PNG")
    buffer.seek(0)
    
    # Return the image as a FileResponse
    return FileResponse(buffer, media_type="image/png")