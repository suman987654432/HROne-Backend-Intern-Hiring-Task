from pydantic import BaseModel, Field
from typing import List

class SizeSchema(BaseModel):
    size: str = Field(..., example="M")
    quantity: int = Field(..., example=10)

class ProductCreate(BaseModel):
    name: str = Field(..., example="T-Shirt")
    price: float = Field(..., example=100.0)
    sizes: List[SizeSchema]

class ProductResponse(BaseModel):
    id: str
    name: str
    price: float


