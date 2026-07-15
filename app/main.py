from fastapi import FastAPI

from app.db.session import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
