import pandas as pd
from sqlalchemy import create_engine

DB_USER = 'user'
DB_PASSWORD = 'password'
DB_HOST = 'postgres'
DB_PORT = '5432'
DB_NAME = 'mydatabase'

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)

