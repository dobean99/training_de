from fastapi import FastAPI
from app.routers import user_router, product_router

app  = FastAPI(title='Training DE', version = "0.0.1",)
@app.get("/")
def roots():
    return {"message": "Welcome to FastAPI Modular Example!"}
app.include_router(user_router.router)
app.include_router(product_router.router)
