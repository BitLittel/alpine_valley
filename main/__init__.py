from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

main = FastAPI(title='Bubble')
main.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# origins = [
#     "http://localhost",
#     "http://localhost:8000",
#     "http://альпийскиеимения.рф",
#     "https://альпийскиеимения.рф",
#     "https://localhost",
#     "https://localhost:8000"
# ]

main.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


from main.views import views
from main.api import submit
