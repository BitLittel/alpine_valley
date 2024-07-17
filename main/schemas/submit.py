from pydantic import BaseModel, field_validator
import re
from fastapi import HTTPException


class Submit(BaseModel):
    name: str
    tel_number: str
    email: str
    comment: str

    @field_validator("name")
    def check_name(cls, value):
        if re.search(r"^[а-яА-ЯёЁ]{2,}$", value) is None:
            raise HTTPException(
                status_code=400,
                detail={'result': False, 'message': 'Имя введено не корректно', 'data': {}}
            )
        return value

    @field_validator("email")
    def check_email(cls, value):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
            raise HTTPException(
                status_code=400,
                detail={'result': False, 'message': 'Почта введена не корректно', 'data': {}}
            )
        return value

    @field_validator("tel_number")
    def check_tel_number(cls, value):
        try:
            value = value.strip().replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        except:
            raise HTTPException(
                status_code=400,
                detail={'result': False, 'message': 'Номер телефона введён не корректно', 'data': {}}
            )
        if re.search(r'^(([+][0-9]{1,3})[0-9]{10})|(8+[0-9]{10})$', value) is None:
            raise HTTPException(
                status_code=400,
                detail={'result': False, 'message': 'Номер телефона введён не корректно', 'data': {}}
            )
        return value[-10:]
