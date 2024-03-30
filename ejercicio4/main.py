from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette import status

from src.dates import get_current_date
from src.authentication import verify_password
from src.database_config import get_db

app = FastAPI()


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/authenticate")
async def login_for_access_token(request: LoginRequest, db: Session = Depends(get_db)) -> dict:
    query = text("SELECT * FROM user WHERE username = :username")
    user = db.execute(query, {"username": request.username}).fetchone()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return {"Authentication": True}


@app.get("/remainingMinutesNonTestable")
async def remaining_minutes_in_year_non_testable() -> dict:
    now = datetime.now()
    adjusted_end_of_year = datetime(now.year + 1, 1, 1, 0, 0, 0)
    adjusted_time_difference = adjusted_end_of_year - now
    # Convert the time difference to minutes
    adjusted_remaining_minutes = adjusted_time_difference.total_seconds() / 60
    return {"remaining_minutes": adjusted_remaining_minutes}


@app.get("/remainingMinutesTestable")
async def remaining_minutes_in_year() -> dict:
    now = get_current_date()
    adjusted_end_of_year = datetime(now.year + 1, 1, 1, 0, 0, 0)
    adjusted_time_difference = adjusted_end_of_year - now
    # Convert the time difference to minutes
    adjusted_remaining_minutes = adjusted_time_difference.total_seconds() / 60
    return {"remaining_minutes": adjusted_remaining_minutes}
