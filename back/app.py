
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import scraping

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scraping.router)


if __name__ == "__main__":
    uvicorn.run(app="app :app", host="0.0.0.0", port=8000, reload=True)
