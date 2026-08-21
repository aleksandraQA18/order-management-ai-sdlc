from fastapi import FastAPI
import psycopg
import os

app = FastAPI()

conn = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)


@app.get("/")
def read_root():
    return {"message": "Order Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
