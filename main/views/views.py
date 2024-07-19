# -*- coding: utf-8 -*-
import time
from main import main, templates
from fastapi import Request, status, HTTPException
from fastapi.exceptions import ValidationException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse


@main.exception_handler(ValidationException)
async def validation_exeption_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'detail': exc.errors()})
    )


@main.exception_handler(HTTPException)
def http_exception(_, exc: HTTPException):
    return JSONResponse(content=exc.detail, headers=exc.headers, status_code=exc.status_code)


@main.middleware("http")
async def before_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@main.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})


@main.get("/panorama", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("panorama.html", context={"request": request})

