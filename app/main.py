from fastapi import FastAPI, Query
from .ai_agent import runAIModel



app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/")
async def read_item(
    destination: str = Query(..., description="旅行目的地"),
    days: int = Query(..., description="旅行天数")
):
    return runAIModel(str, int)
