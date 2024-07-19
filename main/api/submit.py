from main import main
from fastapi import Request, Cookie, Response
from main.schemas.submit import Submit
from main.utils.submit import process_submit
from main.schemas.response import DefaultResponse


@main.post('/api/submit', response_model=DefaultResponse, status_code=201, tags=['Submit'])
async def api_submit(form_submit: Submit, request: Request, response: Response, token=Cookie(default=None)):
    print(form_submit, request)
    token = None
    await process_submit(form_submit=form_submit, request=request, token=token, response=response)
    return {'result': True, 'message': 'Вы успешно оставили заявку, с вами позже свяжутся', 'data': {}}
