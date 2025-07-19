from pydantic import BaseModel, Field
from typing import List

class OrderItem(BaseModel):
    productId: str = Field(..., example="1234567890")
    qty: int = Field(..., example=2)

class OrderCreate(BaseModel):
    userId: str = Field(..., example="user_1")
    items: List[OrderItem]

class OrderResponse(BaseModel):
    id: str
