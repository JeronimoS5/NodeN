from pydantic import BaseModel
from datetime import date

class Person(BaseModel):
    id: str
    name: str
    gender: str  # 'M' o 'F'
    birthdate: date
    location_code: str
    type_doc: str
    parent_id: str | None = None
