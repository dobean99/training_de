from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user_router, product_router

# Create tables in the database
Base.metadata.create_all(bind=engine)

app  = FastAPI(title='Training DE', version = "0.0.1",)
@app.get("/")
def roots():
    return {"message": "Welcome to FastAPI Modular Example!"}
app.include_router(user_router.router)
app.include_router(product_router.router)
