import pandas as pd
import os
import psycopg2
import datetime as dt
import sqlalchemy as sa
import sys
import numpy as np


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

str_connection = 'postgresql://postgres:Andes420.@localhost:5432/postgres'
engine = create_engine(str_connection)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()


