from fastapi import FastAPI
from . import tester

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(tester.router)
