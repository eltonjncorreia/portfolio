from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()
app.mount('/static', StaticFiles(directory='src/static'), name='static')
templates = Jinja2Templates(directory='src/templates')


@app.get('/')
def home(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse(name='home/index.html', context=context)
