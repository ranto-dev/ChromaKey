import os
import requests
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from io import BytesIO

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Get the API key from an environment variable for security
API_KEY = "700d9fa9-9c32-4956-a06d-b96b92ef1a02"

if not API_KEY:
    print("WARNING: REMBG_API_KEY environment variable is not set.")
    # You might want to handle this more gracefully, e.g., by returning an error response.

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/remove-bg/")
async def remove_background(file: UploadFile = File(...)):
    if not API_KEY:
        return {"error": "API key not configured."}

    # Headers with your API key
    headers = {
        "x-api-key": API_KEY
    }

    # Prepare the image file for the API request
    # Since UploadFile is an async file, we need to read it asynchronously.
    image_data = await file.read()
    files = {
        "image": (file.filename, image_data, file.content_type)
    }

    # API configuration and options
    data = {
        "format": "png",  # We'll request a PNG to maintain transparency
        # Add other optional parameters as needed
    }

    try:
        # Send the POST request to the external API
        response = requests.post("https://api.rembg.com/rmbg", headers=headers, files=files, data=data)

        if response.status_code == 200:
            # The API returns the processed image content directly
            buffer = BytesIO(response.content)
            buffer.seek(0)
            return StreamingResponse(buffer, media_type="image/png")
        else:
            # Handle API errors
            error_message = f"API Error: {response.status_code} - {response.text}"
            print(error_message)
            return {"error": error_message}

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return {"error": "Failed to connect to the external API."}
    except Exception as e:
        print(f"Server Error: {e}")
        return {"error": "An unexpected error occurred on the server."}