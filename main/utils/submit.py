from main.models.database import Feedbacks, Tokens
from fastapi import Request, HTTPException, Response
from main.schemas.submit import Submit
from main import config
from uuid import uuid4
import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta


async def send_mail_async(subject, text):
    msg = MIMEMultipart()
    msg.preamble = subject
    msg['Subject'] = subject
    msg['From'] = config.MAIL_USER
    msg['To'] = config.MAIL_USER  # todo: Изменить на почту Константина
    msg.attach(MIMEText(text, 'html', 'utf-8'))
    smtp = aiosmtplib.SMTP(hostname=config.MAIL_HOST, port=config.MAIL_PORT, start_tls=False)
    await smtp.connect()
    if config.MAIL_TLS:
        await smtp.starttls()
    await smtp.login(config.MAIL_USER, config.MAIL_PASSWORD)
    await smtp.send_message(msg)
    await smtp.quit()


async def wrap_send_message(name: str, tel_number: str, email: str, comment: str):
    format_message = f'<h1>Вам поступила заявка</h1>' \
                     f'<p><b>Имя:</b> {name}</p>' \
                     f'<p><b>Телефон: </b> {tel_number}</p>' \
                     f'<p><b>Почта: </b> {email}</p>' \
                     f'<p><b>Комментарий: </b> {comment}</p>'
    await send_mail_async(subject='Notification', text=format_message)


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

    await wrap_send_message(
        name=form_submit.name,
        tel_number=form_submit.tel_number,
        email=form_submit.email,
        comment=form_submit.comment
    )

    await Feedbacks.add_(
        name=form_submit.name,
        tel_number=form_submit.tel_number,
        email=form_submit.email,
        comment=form_submit.comment,
        user_agent=user_agent
    )
