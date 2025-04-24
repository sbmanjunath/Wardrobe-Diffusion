from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import Response
import shutil
from pathlib import Path
import uuid
import uvicorn

from PyVirtry.VirtualTryOn import models

model = models.IDMVTON()

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

@app.post("/process/")
async def upload_images(
    person: UploadFile = File(...), 
    cloth: UploadFile = File(...), 
    optional_text: str = Form(None)
):
    """
    Accepts two images and an optional string. 
    Saves the images with unique filenames.
    """
    
    # Generate unique filenames
    img1_filename = f"{uuid.uuid4().hex[:10]}.jpg"
    img2_filename = f"{uuid.uuid4().hex[:10]}.jpg"
    img1_path = UPLOAD_DIR / img1_filename
    img2_path = UPLOAD_DIR / img2_filename
    
    # Save first image
    with img1_path.open("wb") as buffer:
        shutil.copyfileobj(person.file, buffer)
    
    # Save second image
    with img2_path.open("wb") as buffer:
        shutil.copyfileobj(cloth.file, buffer)
    
    # Process the images to generate 'out.jpg' (for now, just copying one image as a placeholder)
    out_fname = f"{uuid.uuid4().hex[:10]}.jpg"
    result = model.start_tryon(human_img_path = f'uploads/{img1_filename}',
                           garm_img_path = f'uploads/{img2_filename}', 
                           garment_des = 'dress',
                           output_path= f'outputs/{out_fname}')
    
    with open(f'outputs/{out_fname}', "rb") as img_file:
        img_data = img_file.read()
    
    return Response(content=img_data, media_type="image/jpeg")


if __name__ == "__main__":
    
    # Start the FastAPI server
    uvicorn.run(app, host="localhost", port=8080)

