from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import shutil
import os

from app.services.ai_service import AIService

# Initialize App
app = FastAPI(title="Pickabook Python")

# Mount Static Files (CSS, JS)
# This allows us to serve files from /static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup Templates (Jinja2)
# This looks for HTML files in the /templates directory
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def read_root(request: Request):
    """
    Serves the main frontend page.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/generate")
async def generate_image(
    file: UploadFile = File(...),
    style: str = Form("watercolor")
):
    """
    API Endpoint called by the frontend JS.
    """
    if not file.content_type.startswith("image/"):
        return JSONResponse(status_code=400, content={"error": "Invalid file type. Please upload an image."})

    try:
        # We pass the file object directly to the service
        # FastAPI's UploadFile.file is a Python file-like object compatible with Replicate
        image_url = AIService.generate_illustration(file.file, style)
        
        return {"status": "success", "image_url": image_url}
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})