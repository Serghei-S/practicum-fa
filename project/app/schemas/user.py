from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: int
    email: EmailStr


class UserLogin(BaseModel):
    username: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserToken(UserResponse):
    token: Token


class UserCreate(BaseModel):
    email: EmailStr
    password: str
