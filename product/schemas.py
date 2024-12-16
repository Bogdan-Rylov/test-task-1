from datetime import datetime
import regex as re

from pydantic import BaseModel, Field, field_validator, PositiveFloat


class ProductBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    description: str = Field(min_length=5, max_length=1024)
    price: PositiveFloat

    @field_validator("name")
    def validate_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Field cannot be empty or whitespace.")

        pattern = r"^\p{L}[\p{L}0-9 \-']*$"
        if not re.match(pattern, value):
            raise ValueError(
                "The string must start with a letter and can only contain "
                "letters, numbers, spaces, hyphens, and apostrophes."
            )

        return value


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
