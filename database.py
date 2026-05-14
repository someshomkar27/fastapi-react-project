from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 


db_url = "postgresql://postgres:Somesh200%40@127.0.0.1:5432/ecommerce"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind= engine)