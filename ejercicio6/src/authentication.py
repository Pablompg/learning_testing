import bcrypt
from sqlalchemy import text
from sqlalchemy.orm import Session


def get_password_hash(password):
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf8'), hashed_password.encode('utf8'))


def is_user_authenticated(username: str, password: str, db_session: Session) -> bool:
    query = text("SELECT * FROM users WHERE username = :username")
    user = db_session.execute(query, {"username": username}).fetchone()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return True
