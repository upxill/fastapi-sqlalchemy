# FastAPI Product Management API

A simple REST API built with FastAPI and SQLAlchemy for managing product inventory.

## Features

- **Get all products** - Retrieve a list of all products from the database
- **Get product by ID** - Retrieve a specific product by its ID
- **Add product** - Create a new product in the database
- **Update product** - Modify an existing product
- **Delete product** - Remove a product from the database
- **Greeting endpoint** - Simple test endpoint

## Project Structure

```
├── main.py                 # Main FastAPI application with all endpoints
├── models.py              # Pydantic models for API request/response validation
├── database_models.py     # SQLAlchemy ORM models for database operations
├── database.py            # Database configuration and session setup
└── README.md              # This file
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

### 1. Clone or navigate to the project directory
```bash
cd /Users/polagani/Documents/01-workspace/03-fastapi
```

### 2. Create a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install fastapi
pip install sqlalchemy
pip install uvicorn
pip install pydantic
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **fastapi** | Latest | Web framework for building APIs |
| **sqlalchemy** | Latest | ORM for database operations |
| **uvicorn** | Latest | ASGI server to run the FastAPI application |
| **pydantic** | Latest | Data validation using Python type annotations |

## Running the Application

### Start the server
```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

### Interactive API documentation
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## API Endpoints

### 1. Greeting Endpoint
```
GET /app
```
Returns a greeting message.

**Response:**
```json
{
  "message": "Hello from FastAPI!"
}
```

### 2. Get All Products
```
GET /products
```
Retrieves all products from the database.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 999.99,
    "quanity": 10
  },
  {
    "id": 2,
    "name": "Smartphone",
    "price": 499.99,
    "quanity": 25
  }
]
```

### 3. Get Product by ID
```
GET /products/{product_id}
```
Retrieves a specific product by ID.

**Example:** `GET /products/1`

**Response:**
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99,
  "quanity": 10
}
```

### 4. Add Product
```
POST /products
```
Adds a new product to the database.

**Request body:**
```json
{
  "id": 4,
  "name": "Monitor",
  "price": 299.99,
  "quanity": 20
}
```

**Response:**
```json
{
  "message": "Product added successfully",
  "product": {
    "id": 4,
    "name": "Monitor",
    "price": 299.99,
    "quanity": 20
  }
}
```

### 5. Update Product
```
PUT /products/{product_id}
```
Updates an existing product.

**Example:** `PUT /products/1`

**Request body:**
```json
{
  "id": 1,
  "name": "Laptop Pro",
  "price": 1299.99,
  "quanity": 5
}
```

**Response:**
```json
{
  "message": "Product updated successfully",
  "product": {
    "id": 1,
    "name": "Laptop Pro",
    "price": 1299.99,
    "quanity": 5
  }
}
```

### 6. Delete Product
```
DELETE /products/{product_id}
```
Deletes a product from the database.

**Example:** `DELETE /products/1`

**Response:**
```json
{
  "message": "Product deleted successfully"
}
```

## Database

This application uses **SQLite** for data storage. The database file `test.db` will be automatically created in the project directory when the application starts.

- **Database URL:** `sqlite:///./test.db`
- **Location:** Project root directory

## Notes

- The database is configured with SQLite and `connect_args={"check_same_thread": False}` to support concurrent requests in development
- Products are created with sample data on application startup
- The API uses Pydantic models for request validation and SQLAlchemy models for database operations
- All endpoints use proper dependency injection for database session management

## Troubleshooting

### Module not found errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Port already in use
Run on a different port:
```bash
uvicorn main:app --reload --port 8001
```

### Database locked errors
This can happen with SQLite in concurrent scenarios. The current configuration already includes the fix: `connect_args={"check_same_thread": False}`

## License

This project is open source and available for educational purposes.
