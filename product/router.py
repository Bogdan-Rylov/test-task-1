from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from product import schemas, crud
from product.crud import ProductNotFoundError


router = APIRouter()


@router.get("/products/", response_model=list[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    return crud.get_all_products(db=db)


@router.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product_by_id(db=db, product_id=product_id)


@router.post("/products/", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    try:
        return crud.create_product(db=db, product_data=product)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.put("/products/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    try:
        updated_product = (
            crud.update_product(
                db=db, product_id=product_id, product_data=product
            )
        )
    except ProductNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    return updated_product


@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_product(db=db, product_id=product_id)
    except ProductNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    return {"detail": f"Product with ID {product_id} has been deleted"}
