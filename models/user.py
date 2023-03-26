from config.db import engine, meta, Base
from sqlalchemy import Column, Table, ForeignKey, DateTime
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func
from datetime import datetime

tbl_users = Table('tbl_users', meta, 
    Column('id', Integer, primary_key = True),
    Column('name', String(255)),
    Column('user_name',  String(255)),
    Column('email',  String(255)),
    Column('password',  String(255)),
    Column('status',  Integer),
)