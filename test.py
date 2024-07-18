import asyncio
import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MAIL_PARAMS = {
    'TLS': True,
    'host': 'smtp.yandex.ru',
    'password': 'jvgjaqtcnigtgeys',
    'user': 'alp1ne.valley@yandex.ru',
    'port': 587
}
# asset_management@inbox.ru


async def send_mail_async(sender, to, subject, text, textType='html', **params):
    cc = params.get("cc", [])
    bcc = params.get("bcc", [])
    mail_params = params.get("mail_params", MAIL_PARAMS)

    msg = MIMEMultipart()
    msg.preamble = subject
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(to)

    if len(cc):
        msg['Cc'] = ', '.join(cc)
    if len(bcc):
        msg['Bcc'] = ', '.join(bcc)

    msg.attach(MIMEText(text, textType, 'utf-8'))

    # Contact SMTP server and send Message
    host = mail_params.get('host', 'localhost')
    isSSL = mail_params.get('SSL', False)
    isTLS = mail_params.get('TLS', True)
    if isSSL and isTLS:
        raise ValueError('SSL and TLS cannot both be True')
    port = mail_params.get('port', 465 if isSSL else 25)
    # For aiosmtplib 3.0.1 we must set argument start_tls=False
    # because we will explicitly be calling starttls ourselves when
    # isTLS is True:
    smtp = aiosmtplib.SMTP(hostname=host, port=port, start_tls=False, use_tls=isSSL)
    await smtp.connect()
    if isTLS:
        await smtp.starttls()
    if 'user' in mail_params:
        await smtp.login(mail_params['user'], mail_params['password'])
    await smtp.send_message(msg)
    await smtp.quit()


async def main():
    co1 = send_mail_async(
        sender='alp1ne.valley@yandex.ru',
        to=['asset_management@inbox.ru'],
        subject='Notification',
        text='<h1>Привет. Раз раз проверка связи...</h1>'
    )
    await asyncio.gather(co1)

if __name__ == "__main__":
    asyncio.run(main())
