from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

FILE_PATH = "/home/andy/ws/ctpsws/lessons/src/lessons/jennniferj/assign/"

engine = create_engine(f"sqlite:///{FILE_PATH}inventory.db", echo=False)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Brands(Base):
    __tablename__ = "brands"
    brand_id = Column(Integer, primary_key=True)
    name = Column(String)

    products = relationship("Product", backref="Brands")

    def __repr__(self):
        return f"Product Name: {self.name} Price: {self.price} " \
               f"Quantity: {self.quantity} Updated: {self.updated} " \
               f"Brand: {self.brand}"


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    updated = Column(Date)
    brand_id = Column(Integer, ForeignKey("brands.brand_id"))
