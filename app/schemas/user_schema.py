from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    #Pydantic configuration class that changes how your model behaves.
    class Config: 
        from_attributes= True