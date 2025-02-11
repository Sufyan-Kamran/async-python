from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/a", response_class=HTMLResponse)
async def home1(request: Request):
    await asyncio.sleep(10)
    print(1)
    return templates.TemplateResponse("index1.html", {"request": request})