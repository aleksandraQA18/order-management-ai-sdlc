from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes.products import router as products_router
from app.database import check_database_connection

app = FastAPI()
app.include_router(products_router)


@app.get("/")
def read_root():
    return {"message": "Order Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "OK"}


@app.get("/ready")
def readiness_check():
    if check_database_connection():
        return {"status": "ready"}
    return JSONResponse(status_code=503, content={"status": "not ready"})
