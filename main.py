from fastapi import FastAPI, Response, status, HTTPException, Depends
import psycopg2
import models
from sqlalchemy.orm import Session
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sqlalchemy")
def test_posta(db: Session = Depends(get_db)):
    return {"status": "success"} 