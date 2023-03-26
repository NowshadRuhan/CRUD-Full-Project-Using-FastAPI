from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Table, ForeignKey, DateTime

class User(BaseModel): 
    name: str
    user_name: str
    email: str
    password: str
    status: int
