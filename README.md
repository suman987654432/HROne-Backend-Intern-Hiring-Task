# E-Commerce Backend API

FastAPI + MongoDB e-commerce backend with product and order management.

## 🌐 Live API
**URL**: https://hrone-backend-intern-hiring-task.onrender.com  
**Docs**: https://hrone-backend-intern-hiring-task.onrender.com/docs

## 🚀 Quick Start
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🔌 API Endpoints

### Products
- `POST /products/` - Create product
- `GET /products/` - List products (filterable by name, size)

### Orders
- `POST /orders/` - Create order
- `GET /orders/` - List all orders
- `GET /orders/{user_id}` - Get user orders

## 📁 Project Structure
```
app/
├── main.py              # FastAPI app
├── database.py          # MongoDB connection
├── routes/              # API endpoints
├── schemas/             # Pydantic models
└── utils/               # Pagination utilities
```

## 🧪 Testing

**Create Product:**
```bash
curl -X POST "https://hrone-backend-intern-hiring-task.onrender.com/products/" \
  -H "Content-Type: application/json" \
  -d '{"name": "T-Shirt", "price": 25.99, "sizes": [{"size": "M", "quantity": 10}]}'
```

**List Products:**
```bash
curl "https://hrone-backend-intern-hiring-task.onrender.com/products/"
```

**Create Order:**
```bash
curl -X POST "https://hrone-backend-intern-hiring-task.onrender.com/orders/" \
  -H "Content-Type: application/json" \
  -d '{"userId": "user123", "items": [{"productId": "YOUR_PRODUCT_ID", "qty": 1}]}'
```

## 📝 Response Format
```json
{
  "data": [...],
  "page": {
    "limit": 10,
    "offset": 0,
    "next": 10,
    "previous": null
  }
}
```

## 📄 License
This project is licensed under the MIT License.

## 🆘 Support
For support and questions:
- Create an issue in the repository
- Check the API documentation at `/docs`

---
**Built with FastAPI & MongoDB** 🚀
