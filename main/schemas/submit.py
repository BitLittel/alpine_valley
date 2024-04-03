from pydantic import BaseModel


class Submit(BaseModel):
    phone: str
    fio: str
    question: str
