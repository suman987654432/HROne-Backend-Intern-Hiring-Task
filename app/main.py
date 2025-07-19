from fastapi import FastAPI
from app.routes import product_routes, order_routes
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(redirect_slashes=False)


app.include_router(product_routes.router)
app.include_router(order_routes.router)

@app.get("/")
def root():
    return {"message": "API is running"}
