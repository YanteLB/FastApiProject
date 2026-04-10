
from fastapi import FastAPI, HTTPException, status
from models import Product
from database import (
    add_product,
    delete_product,
    get_product_by_id,
    get_products,
    update_product,
)

app = FastAPI() 

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/products")
def get_all_products():
    return get_products()

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = get_product_by_id(product_id)
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found",
    )

@app.post("/products")
def create_product(product: Product):
    try:
        return add_product(product)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc


@app.put("/products/{product_id}")
def put_product(product_id: int, product: Product):
    try:
        updated_product = update_product(product_id, product)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    if not updated_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return updated_product


@app.delete("/products/{product_id}")
def remove_product(product_id: int):
    deleted_product = delete_product(product_id)
    if not deleted_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return deleted_product
  