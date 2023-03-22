""" Module for DTO definitions
"""

from pydantic import BaseModel
from typing import List


class RootContentDto(BaseModel):
    message: str
    version: str


class CarsDto(BaseModel):
    owner: str
    brand: str
    model: str


class CarsListDto(BaseModel):
    status: str
    cars: List[CarsDto]
