
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import scraping
import news

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scraping.router)
app.include_router(news.router)

if __name__ == "__main__":
    uvicorn.run(app="app :app", host="0.0.0.0", port=8000, reload=True)
