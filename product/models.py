from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.sql import func

from database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(Text, nullable=True, unique=True)
    price = Column(Float(precision=2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
