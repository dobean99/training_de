from fastapi import APIRouter,HTTPException
from app.models.product_model import Product,ProductCreate

router = APIRouter(prefix="/product",tags=["Products"])

product = []

@router.post("/",response_model=Product)
def create_product(product:ProductCreate):
    new_product = Product(id=len(product)+1,**product.model_dump())
    product.append(new_product)
    return new_product