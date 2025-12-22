from sqlalchemy.exc import IntegrityError
from typing import List
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserResponse
from app.tasks.email_tasks import send_welcome_email

router = APIRouter(prefix="/users", tags=["Users"])


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# def create_user(
#     user: UserCreate,
#     db: Session = Depends(get_db),
#     background_tasks: BackgroundTasks = Depends(),
# ):
#     # Optional pre-check (still keep DB UNIQUE constraint to avoid races)
#     existing = db.query(User).filter(User.email == user.email).first()
#     if existing:
#         raise HTTPException(status_code=409, detail="Email already registered")

#     db_user = User(name=user.name, email=user.email)
#     db.add(db_user)
#     try:
#         db.commit()
#     except IntegrityError:
#         db.rollback()
#         # Catches duplicate email if another request slipped in between
#         raise HTTPException(status_code=409, detail="Email already registered")
#     db.refresh(db_user)

#     # Fire-and-forget background job
#     background_tasks.add_task(send_email, db_user.email)

#     return db_user


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print("User created")
    send_welcome_email(user.email)
    return db_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    # no have => None => exception
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_user: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = updated_user.name
    user.email = updated_user.email

    db.commit()
    db.refresh(user)
    return user
