from __future__ import annotations
from typing_extensions import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
import sqlalchemy as sa
from sqlalchemy.orm import joinedload

from app.core.database import get_db

from app.models.user import User
from app.models.role import Role

from app.schemas.user import UserOut, UserCreate, UserUpdate

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

router = APIRouter()

def to_user_out(u: User) -> UserOut:
    return UserOut(id=u.id, username=u.username, role=u.role.name)

@router.get("", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.scalars(
        sa.select(User).options(joinedload(User.role)).order_by(User.id)
    ).all()

    return [to_user_out(u) for u in users]

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.scalar(
        sa.select(User).where(User.id == user_id).options(joinedload(User.role))
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return to_user_out(user)

@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    role_exists = db.scalar(sa.select(1).where(Role.id == payload.role_id))
    if not role_exists:
        raise HTTPException(status_code=400, detail="Role not found'")
    
    login_exists = db.scalar(sa.select(1).where(User.login == payload.login))
    if login_exists:
        raise HTTPException(status_code=409, detail="Login already exists")
    
    user = User(
        username=payload.username,
        login=payload.login,
        password=payload.password,
        role_id=payload.role_id
    )
    db.add(user)
    db.commit()

    db.refresh(user)
    user = db.scalar(
        sa.select(User).where(User.id == user.id).options(joinedload(User.role))
    )
    return to_user_out()

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.scalar(sa.select(User).where(User.id == user_id))
    if not user:
        return HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()

    return None