from fastapi import APIRouter, HTTPException, Depends, Request, Response, Form
from sqlmodel import select
from app.database import SessionDep
from app.models import *
from app.utilities import flash
from app.auth import encrypt_password, verify_password, create_access_token, AuthDep
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import status
from . import templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.schemas.user import UserResponse
from app.models.user import User
from app.utilities.flash import flash
from app.schemas.user import RegularUserCreate


users_router = APIRouter()

@users_router.get("/users")
async def users(
    request: Request,
    user: AuthDep,
    db:SessionDep
):
    users = db.exec(select(User)).all()
    return templates.TemplateResponse(
        request=request, 
        name="users.html",
        context={
            "user": user,
            "all_users": users
        }
    )