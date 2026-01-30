from pydantic import BaseModel, Field

class UserOut(BaseModel):
    id:int
    username:str
    role:str

    model_config = {"from_attributes": True}

class UserCreate(BaseModel):
    username: str = Field(min_length=1)
    login: str = Field(min_length=1)
    password: str = Field(min_length=1)
    role_id: int

class UserUpdate(BaseModel):
    username: str | None = None
    login: str | None = None
    password: str | None = None
    role_id: int | None = None