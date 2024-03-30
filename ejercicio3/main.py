from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def is_palindrome_endpoint(input: str) -> dict:
    return {"palindrome": input == input[::-1]}
