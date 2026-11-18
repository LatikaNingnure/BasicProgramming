FastAPI Application Development

This repository contains basic application development using FastAPI and Python. It covers REST API development, HTTP methods, request and response handling, data validation, and API documentation.

🚀 Technologies Used
Python
FastAPI
Uvicorn
Pydantic
📌 Concepts Covered
Introduction to FastAPI
Creating FastAPI applications
GET, POST, PUT, PATCH, and DELETE methods
Path parameters
Query parameters
Request body handling
Data validation using Pydantic
Response models
HTTP status codes
Exception handling
Automatic API documentation
📂 Project Structure
text
fastapi-application/
│
├── main.py
├── requirements.txt
└── README.md

⚙️ Installation and Setup
1. Clone the repository
bash
git clone https://github.com/YOUR_USERNAME/fastapi-application.git

2. Navigate to the project directory
bash
cd fastapi-application

3. Create a virtual environment
bash
python -m venv venv

4. Activate the virtual environment

Windows:

bash
venv\Scripts\activate


Linux / macOS:

bash
source venv/bin/activate

5. Install dependencies
bash
pip install fastapi uvicorn

6. Run the application
bash
uvicorn main:app --reload

🌐 API Documentation

After starting the application, access the following URLs:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
🔗 HTTP Methods
Method	Description
GET	Retrieve data
POST	Create new data
PUT	Update existing data
PATCH	Partially update data
DELETE	Delete data
💡 Sample FastAPI Application
python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.post("/users")
def create_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }

🎯 Objective

The objective of this repository is to understand the fundamentals of FastAPI and learn how to develop simple REST APIs using Python.

📚 Reference

Official FastAPI Documentation: https://fastapi.tiangolo.com/

Developed using Python and FastAPI.
