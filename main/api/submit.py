from main import main
from main.schemas.response import DefaultResponse


@main.get('/api/submit', response_model=DefaultResponse)
async def api_submit():
    return {'result': True, 'message': 'Успех', 'data': {}}
