from fastapi import FastAPI
import uvicorn
from app.api import router as api_router

app = FastAPI()

app.include_router(api_router, tags=["api"], prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)