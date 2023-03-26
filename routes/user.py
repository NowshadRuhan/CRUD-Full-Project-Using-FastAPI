from config.db import conn
from fastapi import APIRouter
from models.index import tbl_users
from schemas.index import User
from passlib.context import CryptContext


our_user = APIRouter()


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

@our_user.get('/')
async def fetch_users():
    query = tbl_users.select()
    data = conn.execute(query).fetchall()
    print(type(data))
    # return {'name':'nowshad'}
    return data
    # return conn.execute(tbl_users.select()).fetchall()

@our_user.post("/add-user")
async def write_user_date(user: User):
    conn.execute(tbl_users.insert().values(
        name = user.name,
        user_name = user.user_name,
        email = user.email,
        password = get_password_hash(user.password),
        status = 1
    ))
    return conn.execute(tbl_users.select()).fetchall()



@our_user.get("/get-user-by-id/{id}")
async def get_user_date(id:int):
    return conn.execute(tbl_users.select().where(tbl_users.c.id == id)).fetchall()



@our_user.put("/update-user/{id}")
async def update_user_date(id:int, user: User):
    conn.execute(tbl_users.update().values(
        name = user.name,
        user_name = user.user_name,
        email = user.email,
        password = get_password_hash(user.password),
        status = 1
    ).where(tbl_users.c.id==id))
    return conn.execute(tbl_users.select().where(tbl_users.c.id == id)).fetchall()


@our_user.delete("/delete-user/{id}")
async def delete_user_date(id:int):
    conn.execute(tbl_users.delete().where(tbl_users.c.id == id))
    return conn.execute(tbl_users.select()).fetchall()