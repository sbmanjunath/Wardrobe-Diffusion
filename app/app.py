from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_images(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    file1_path = os.path.join(UPLOAD_DIR, file1.filename)

    # Save the first image
    with open(file1_path, "wb") as buffer:
        shutil.copyfileobj(file1.file, buffer)

    return FileResponse(file1_path, media_type="image/png")