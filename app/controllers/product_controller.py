from fastapi import APIRouter, HTTPException
from app.models.products import Product, ProductModel
from app.repositories.product_repositories import product_repository

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=Product, status_code=201)
def create_product(product_data: ProductModel):
    # Check if SKU already exists
    existing_product = get_product_by_sku(product_data.sku)
    if existing_product:
        raise HTTPException(status_code=409, detail=f"SKU {product_data.sku} already exists")
    
    # Create product
    return product_repository.create(product_data)

@router.get("/", response_model=list[Product])
def get_all_products():
    return product_repository.get_all()

@router.get("/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    product = product_repository.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def get_product_by_sku(sku: str) -> Product:
    # Helper function to check SKU uniqueness
    for product in product_repository.get_all():
        if product.sku == sku:
            return product
    return None