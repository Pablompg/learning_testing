from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, Form
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse

from src.authentication import is_user_authenticated
from src.database_config import get_db, init_db


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=app_lifespan)


@app.post("/welcome", response_class=HTMLResponse)
async def welcome_page(username: str = Form(...), password: str = Form(...), db_session: Session = Depends(get_db)):
    is_user_valid = is_user_authenticated(username, password, db_session)
    if is_user_valid:
        body_content = f"""
        <body>
            <div class="container">
                <h1>Welcome, {username}!</h1>
            </div>
        </body>
        """
    else:
        body_content = """
            <body>
                <div class="container">
                    <h1>Try <a href="/">here</a>, credentials were not valid.</h1>
                </div>
            </body>
            """
    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Welcome Page</title>
            <!-- Bootstrap CSS CDN for styling -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        </head>
        {body_content}
        </html>
        """
    return HTMLResponse(content=html_content)


@app.get("/", response_class=HTMLResponse)
def login_form():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login Page</title>
        <!-- Bootstrap CSS CDN for styling -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f5f5f5;
            }
            .login-container {
                width: 100%;
                max-width: 400px;
                padding: 15px;
                margin: auto;
            }
            .form-signin {
                width: 100%;
                max-width: 330px;
                padding: 15px;
                margin: auto;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <form class="form-signin" action="/welcome" method="post">
                <h2 class="text-center">Please sign in</h2>
                <label for="username" class="sr-only">Username</label>
                <input type="text" name="username" id="username" class="form-control" placeholder="Username" required autofocus>
                <label for="password" class="sr-only">Password</label>
                <input type="password" name="password" id="password" class="form-control" placeholder="Password" required>
                <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>
            </form>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)