from fastapi import APIRouter, Query, HTTPException
from app.database import db
from app.schemas.order_schema import OrderCreate
from app.utils.pagination import create_pagination_response, validate_pagination_params
from bson import ObjectId
from bson.errors import InvalidId
import logging

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", status_code=201)
async def create_order(order: OrderCreate):
    try:
      
        logging.info(f"Creating order: {order.dict()}")
        
        
        for item in order.items:
           
            if not ObjectId.is_valid(item.productId):
                raise HTTPException(
                    status_code=400, 
                    detail=f"Invalid product ID format: '{item.productId}'. Must be a 24-character hexadecimal string."
                )
            
            try:
                product = await db.products.find_one({"_id": ObjectId(item.productId)})
                if not product:
                    raise HTTPException(status_code=404, detail=f"Product {item.productId} not found")
            except InvalidId:
                raise HTTPException(status_code=400, detail=f"Invalid product ID: {item.productId}")
        
        order_dict = order.dict()
        result = await db.orders.insert_one(order_dict)
        return {"id": str(result.inserted_id)}
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Failed to create order: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to create order: {str(e)}")

# to get all orders 
@router.get("/", status_code=200)
async def get_all_orders(
    limit: int = Query(10),
    offset: int = Query(0)
):
    try:
        offset, limit = validate_pagination_params(offset, limit)
        
        orders_cursor = db.orders.find({}).skip(offset).limit(limit)
        orders = []
        async for order in orders_cursor:
            orders.append({
                "id": str(order["_id"]),
                "userId": order.get("userId"),
                "items": order.get("items", [])
            })
        
        return create_pagination_response(orders, offset, limit)
    except Exception as e:
        logging.error(f"Failed to fetch all orders: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch orders")

# Get List of Orders for a User
@router.get("/{user_id}", status_code=200)
async def get_orders(
    user_id: str,
    limit: int = Query(10),
    offset: int = Query(0)
):
    try:
      
        offset, limit = validate_pagination_params(offset, limit)
        
        orders_cursor = db.orders.find({"userId": user_id}).skip(offset).limit(limit)
        orders = []
        async for order in orders_cursor:
            items = []
            for item in order["items"]:
                try:
                    if ObjectId.is_valid(item["productId"]):
                        product = await db.products.find_one({"_id": ObjectId(item["productId"])})
                        if product:
                            product_details = {"name": product["name"], "id": str(product["_id"])}
                            items.append({"productDetails": product_details, "qty": item["qty"]})
                except (InvalidId, Exception) as e:
                    logging.warning(f"Invalid product ID in order: {item.get('productId')}")
                    continue
            orders.append({"id": str(order["_id"]), "items": items})
        
        return create_pagination_response(orders, offset, limit)
    except Exception as e:
        logging.error(f"Failed to fetch orders for user {user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch orders")
