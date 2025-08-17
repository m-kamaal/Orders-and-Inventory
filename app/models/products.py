from decimal import Decimal
from pydantic import BaseModel, Field

class ProductModel(BaseModel):
    sku: str = Field(min_length=1, max_length=64)
    name: str = Field(min_length=1, max_length=255)
    price: Decimal = Field(gt=0)
    stock: int = Field(ge=0)

class Product(ProductModel):
    id: int  #Because client should not set 