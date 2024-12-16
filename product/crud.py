from sqlalchemy.orm import Session

from product import models, schemas


class ProductNotFoundError(Exception):
    def __init__(self, product_id: int):
        self.product_id = product_id
        super().__init__(f"Product with ID '{product_id}' not found.")


def check_product_uniqueness(
    db: Session,
    product_data: schemas.ProductCreate | schemas.ProductUpdate,
    product_id: int = None,
) -> None:
    query = db.query(models.Product).filter(
        (models.Product.name == product_data.name) |
        (models.Product.description == product_data.description)
    )

    if product_id:
        query = query.filter(models.Product.id != product_id)

    existing_product = query.first()

    if existing_product:
        if existing_product.name == product_data.name:
            raise ValueError(
                f"Product with name '{product_data.name}' already exists."
            )
        if existing_product.description == product_data.description:
            raise ValueError("Product with such description already exists.")


def get_product_by_id(db: Session, product_id: int) -> models.Product | None:
    return (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )


def get_all_products(db: Session) -> list[models.Product]:
    return db.query(models.Product).all()


def create_product(
    db: Session,
    product_data: schemas.ProductCreate
) -> models.Product:
    check_product_uniqueness(db=db, product_data=product_data)

    new_product = models.Product(
        name=product_data.name,
        description=product_data.description,
        price=product_data.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


def update_product(
    db: Session,
    product_id: int,
    product_data: schemas.ProductUpdate
) -> models.Product:
    db_product = (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )

    if not db_product:
        raise ProductNotFoundError(product_id)

    check_product_uniqueness(
        db=db, product_data=product_data, product_id=product_id
    )

    db_product.name = product_data.name
    db_product.description = product_data.description
    db_product.price = product_data.price
    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int) -> None:
    db_product = (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )

    if not db_product:
        raise ProductNotFoundError(product_id)

    db.delete(db_product)
    db.commit()
