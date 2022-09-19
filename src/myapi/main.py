from pathlib import Path

from fastapi import APIRouter, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from mangum import Mangum

from myapi.lib.get_result import get_result

app = FastAPI()

router = APIRouter()


templates = Jinja2Templates(directory=Path(__file__).parent.joinpath("templates"))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


@app.post("/api/v1/endpoint", response_class=HTMLResponse)
async def gimme(request: Request, myquery: str = Form()):

    try:
        text = get_result(myquery)
        image = ""
    except:
        text = ""
        image = "https://img.freepik.com/premium-vector/bomb-pop-art-style-comic-speech-bubble-with-text-boom-cartoon-dynamite-background-with-dots-halftone-sunburst_11554-740.jpg?w=2000"

    context = {
        "request": request,
        "text": text,
        "image": image,
    }
    return templates.TemplateResponse("result.html", context)


handler = Mangum(app)
