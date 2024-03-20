from decimal import Decimal
from pydantic import BaseModel, Field


class ToyModel(BaseModel):
    name: str = Field(min_length=2)
    price: Decimal = Field(gt=0)


class Shelf(BaseModel):
    toys: list[ToyModel]

