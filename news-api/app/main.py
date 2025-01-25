from fastapi import FastAPI
from .routers import news

app = FastAPI()

# Include the news router
app.include_router(news.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News API"}
