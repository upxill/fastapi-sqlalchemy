
from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int 
    name: str
    price: float
    quanity: int
 