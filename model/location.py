from model.parameter import Parameter
from pydantic import BaseModel


class Location(Parameter):
    state_code: str
    state_name: str
    is_capital: bool
