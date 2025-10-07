from fastapi import FastAPI, File, UploadFile
import requests
import os

app = FastAPI()

COPILOT_API_KEY = os.getenv("COPILOT_API_KEY")
COPILOT_ENDPOINT = "https://copilot.microsoft.com/api/image-understanding"

@app.post("/identify")
async def identify_species(image: UploadFile = File(...)):
    headers = {
        "Authorization": f"Bearer {COPILOT_API_KEY}",
        "Content-Type": "application/octet-stream"
    }
    image_bytes = await image.read()
    
    response = requests.post(COPILOT_ENDPOINT, headers=headers, data=image_bytes)
    result = response.json()

    return {
        "species_name": result.get("species_name"),
        "common_name": result.get("common_name")
    }
