
import requests

# Endpoint URL for the background-removal API
url = "https://api.rembg.com/rmbg"

# Required API key header
headers = {
    "x-api-key": "YOUR_API_KEY_HERE"
}

# The image file to process (opened in binary mode)
files = {
    "image": open("/path/to/image.jpg", "rb")
}

# Optional form fields supported by your backend.
# Adjust values as needed; any of these can be omitted.
data = {
    "format": "webp",         # Output format: "webp" (default) or "png"
    "w": 800,                 # Target width (maintains aspect ratio unless exact_resize is true)
    "h": 600,                 # Target height
    "exact_resize": "false",  # "true" forces exact w×h, may distort
    "mask": "false",          # "true" returns only the alpha mask
    "bg_color": "#ffffffff",  # Optional solid background color (RGBA hex)
    "angle": 0,               # Rotation angle in degrees
    "expand": "true",         # Add padding so rotated images aren’t cropped
}

# Send the POST request with headers, file, and extra form data
response = requests.post(url, headers=headers, files=files, data=data)

# Handle the response
if response.status_code == 200:
    # Save the processed image to disk
    with open("output.webp", "wb") as f:
        f.write(response.content)
    print("Background removed successfully → saved as output.webp")
else:
    # Print error details if the request failed
    print("Error:", response.status_code, response.text)
