from fastapi import Depends,FastAPI
from models import Product
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from database import  session,engine
import database_models
from database_models import Base
from sqlalchemy.orm import Session
app = FastAPI()
 
 
database_models.Base.metadata.create_all(bind=engine) 

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/app")
def greet():
     return {"message": "Hello from FastAPI!"}

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    products=db.query(database_models.Product).all()
    return products

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db_product = database_models.Product(
        id=product.id,
        name=product.name,
        price=product.price,
        quanity=product.quanity
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {
        "message": "Product added successfully", "product": product
        }


@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    products=db.query(database_models.Product).all()
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Product not found"}

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product, db: Session = Depends(get_db)):
    products=db.query(database_models.Product).all()
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return {"message": "Product updated successfully", "product": updated_product}

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    products=db.query(database_models.Product).all()
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted successfully"}