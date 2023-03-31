from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BD_URL = config('BD_URL')

engine = create_engine(BD_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)