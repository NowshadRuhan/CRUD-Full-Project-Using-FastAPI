# from sqlalchemy import create_engine, MetaData

# engine = create_engine("mysql+pymysql://root@localhost:3306/crud_database")

# meta = MetaData()
# conn = engine.connect()
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+pymysql://root:password@localhost:3005/doctors_appoinment')

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/crud_database"

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/crud_database"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

meta = MetaData()

conn = engine.connect()

Base = declarative_base()

