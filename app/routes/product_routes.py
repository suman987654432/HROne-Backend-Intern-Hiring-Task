from fastapi import APIRouter, HTTPException, Query
from app.database import db
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.utils.pagination import create_pagination_response, validate_pagination_params
from bson import ObjectId
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", status_code=201)
async def create_product(product: ProductCreate):
    try:
        product_dict = product.dict()
        result = await db.products.insert_one(product_dict)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to create product")


# List Products API
@router.get("/", status_code=200)
async def list_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = Query(10),
    offset: int = Query(0)
):
    try:
       
        offset, limit = validate_pagination_params(offset, limit)
        
        query = {}
        if name:
            query["name"] = {"$regex": name, "$options": "i"}
        if size:
            query["sizes.size"] = size

        products = await db.products.find(query).skip(offset).limit(limit).to_list(length=limit)
        data = [{"id": str(p["_id"]), "name": p["name"], "price": p["price"]} for p in products]

        return create_pagination_response(data, offset, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch products")
