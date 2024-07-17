from main.models.database import Feedbacks, Tokens
from fastapi import Request, HTTPException, Response
from main.schemas.submit import Submit
from uuid import uuid4
from datetime import datetime, timedelta


async def process_submit(response: Response, form_submit: Submit, request: Request, token: str | None = None):
    if token is not None:
        check_token = await Tokens.get_(token=token)
        if check_token:
            if check_token.datetime_create + timedelta(hours=24) > datetime.now():
                raise HTTPException(
                    status_code=400,
                    detail={
                        'result': False,
                        'message': 'Вы уже недавно отправляли заявку, подождите 24 часа',
                        'data': {}
                    }
                )
    try:
        user_agent = request.headers.get('user-agent')
        request_ip = request.headers.get('x-forwarded-for')
    except:
        raise HTTPException(
            status_code=400,
            detail={
                'result': False,
                'message': 'Ах ты хитрец... А-та-та...',
                'data': {}
            }
        )

    check_ip = await Tokens.get_(ip=request_ip)
    if check_ip:
        if check_ip.datetime_create + timedelta(hours=24) > datetime.now():
            raise HTTPException(
                status_code=400,
                detail={
                    'result': False,
                    'message': 'Вы уже недавно отправляли заявку, подождите 24 часа',
                    'data': {}
                }
            )

    await Tokens.del_(ip=request_ip)
    if token is not None:
        await Tokens.del_(token=token)

    new_token = uuid4()
    await Tokens.add_(token=new_token, ip=request_ip, user_agent=user_agent)
    response.set_cookie(key='token', value=new_token, max_age=123, path='/', httponly=True, samesite='strict')

    # todo: send Email

    await Feedbacks.add_(
        name=form_submit.name,
        tel_number=form_submit.tel_number,
        email=form_submit.email,
        comment=form_submit.comment,
        user_agent=user_agent
    )
