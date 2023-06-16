from pydantic import BaseModel

class categorySchema(BaseModel):
    name_tm: str
    name_ru: str


class subcategorySchema(categorySchema):
    category_id: int


class productSchema(BaseModel):
    name_tm = str
    name_ru = str
    category_id: int
    description_tm: str
    description_ru: str
    price: float
    code: str
    discount: float
    subcategory_id: int

class loginSchema(BaseModel):
    email: str
    password: str
    
class registerSchema(loginSchema):
    username: str
    retype_password: str