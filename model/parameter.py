from pydantic import BaseModel

class Parameter(BaseModel):
    code: str
    description: str
