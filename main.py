# from fastapi import FastAPI, Depends
# from db import Base, engine, get_db
# from sqlalchemy.orm import Session
# from models import Users, Car
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# Base.metadata.create_all(engine)

# class UsersSchema(BaseModel):
#     first_name: str
#     last_name: str
#     password: str

# @app.post('/add-user')
# def add_users(user: UsersSchema, db: Session = Depends(get_db)):
#     new_add = Users(
#         first_name = user.first_name,
#         last_name = user.last_name,
#         password = user.password
#     )
#     db.add(new_add)
#     db.commit()
#     db.refresh(new_add)
#     return new_add

# @app.get('/get-users')
# def get_users(db:Session = Depends(get_db)):
#     result = db.query(
#         Users.id,
#         Users.first_name,
#         Users.last_name
#     ).all()
#     return result

# @app.get('/get-user')
# def get_user(name:str, db: Session = Depends(get_db)):
#     result = db.query(
#         Users.id,
#         Users.first_name,
#         Users.last_name
#     ).filter(Users.first_name == name).first()
#     return result

#from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from models import Product, productSchema, productIsDeletedSchema
# from db import Base, engine, get_db

# app = FastAPI()

# Base.metadata.create_all(engine)

# @app.post('/add-product')
# def add_product(product: productSchema, db: Session = Depends(get_db)):
#     new_add = Product(
#         name         = product.name,
#         description  = product.description,
#         location     = product.location,
#         price        = product.price,
#         phone_number = product.phone_number
#     )
#     db.add(new_add)
#     db.commit()
#     db.refresh(new_add)
#     return new_add

# @app.get('/get-products')
# def get_products(db:Session = Depends(get_db)):
#     result = db.query(
#         Product.id,
#         Product.name,
#         Product.description,
#         Product.location,
#         Product.price,
#         Product.phone_number
#     ).filter(Product.is_deleted == False).all()
#     return result

# @app.put('/update-product/{id}')
# def update_product(id:int, product: productSchema, db:Session=Depends(get_db)):
#     new_update = db.query(Product).filter(Product.id == id)\
#     .update({
#         Product.name         : product.name,
#         Product.description  : product.description,
#         Product.location     : product.location,
#         Product.price        : product.price,
#         Product.phone_number : product.phone_number
#     },synchronize_session=False)
#     db.commit()
#     return{'result: Successfully updated!!!'}

# @app.put('/update-product-is-deleted/{id}')
# def update_product_deleted(id: int, delete: productIsDeletedSchema, db:Session = Depends(get_db)):
#     new_update = db.query(Product).filter(Product.id == id)\
#     .update(
#         {
#             Product.is_deleted: delete.is_deleted
#         },synchronize_session=False)
#     db.commit()
#     return{'result': 'Successfully deleted!!!'}

# @app.get('/get-deleted-products')
# def get_deleted(db: Session = Depends(get_db)):
#     result = db.query(
#         Product.id,
#         Product.name,
#         Product.description,
#         Product.location,
#         Product.price,
#         Product.phone_number
#     ).filter(Product.is_deleted == True).all()
#     return result

# @app.delete('/delete-product/{id}')
# def delete_product(id: int, db: Session = Depends(get_db)):
#     new_delete = db.query(Product).filter(Product.id == id)\
#         .delete(synchronize_session=False)
#     db.commit()
#     return{'result': 'Successfully deleted!!!'}

# from fastapi import FastAPI
# from db import Base, engine
# from routers import department_router, employee_router

# app = FastAPI()

# Base.metadata.create_all(engine)

# app.include_router(department_router, tags=['Department'])
# app.include_router(employee_router, tags=['Employee'])

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db import Base, engine
from routers import *

app = FastAPI()

Base.metadata.create_all(engine)

app.mount('/uploads',StaticFiles(directory='uploads'), name='uploads')

app.include_router(category_router, tags=['Category'])
app.include_router(subcategory_router, tags=['subCategory'])
app.include_router(product_router, tags=['Product'])
app.include_router(image_router, tags=['Image'])
app.include_router(authentication_router, tags=['Authentication'])
app.include_router(favourite_router, tags=['Favourites'])
