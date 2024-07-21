from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time
from datetime import datetime

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


@main.middleware("http")
async def before_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["Cache-Control"] = 'no-cache, no-store, must-revalidate, max-age=0'
    response.headers["Pragma"] = 'no-cache'
    response.headers["Expires"] = '0'
    response.headers["Last-Modified"] = datetime.now().isoformat()
    return response


from main.views import views
from main.api import submit
