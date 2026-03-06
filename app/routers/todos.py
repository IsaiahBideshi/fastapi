from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import select
from app.database import SessionDep
from app.models import *
from app.auth import *
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import status
from . import templates

todos_router = APIRouter()

@todos_router.get("/todos", response_class = HTMLResponse)
async def todos(
    request: Request,
    user: AuthDep,
    db:SessionDep
):
    return templates.TemplateResponse(
        request=request, 
        name="todos.html",
        context={
            "user": user
        }
    )