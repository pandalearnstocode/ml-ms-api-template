from pydantic import BaseModel

class MMM(BaseModel):
    id: int
    color: str
    mass: float


class CreateMMM(BaseModel):
    color: str
    mass: float


class UpdateMMM(BaseModel):
    color: str
