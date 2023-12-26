from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.datastructures import FormData

from src.contact.application.managers import ContactDTO
from src.contact.application.managers import ContactManager
from src.db import get_session
from src.models import ContactMessage

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/")
def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(name="home/index.html", context=context)


@router.get("/contact")
def contact(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(name="contact/contact.html", context=context)


@router.post("/contact")
async def contact_create(request: Request, session: Session = Depends(get_session)):

    form: FormData = await request.form()
    name = form.get("name")

    contact_dto: ContactDTO = ContactDTO(**form)

    manager: ContactManager = ContactManager(session)
    contact_model: ContactMessage = manager.create_new_contact(contact_dto)

    context = {"request": request, "contact": contact_model}
    return templates.TemplateResponse(name="contact/contact.html", context=context)
