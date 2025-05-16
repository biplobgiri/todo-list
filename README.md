# 📝 FastAPI Todo App

A simple and efficient **Todo List API** built using **FastAPI**. It allows users to create, retrieve, and delete tasks using RESTful endpoints. Perfect for learning or building as a microservice.

---

## 🚀 Features

- Create todos
- View all todos
- Delete todos
- Lightweight and fast API using FastAPI
- Built-in validation using Pydantic
- Easily testable using `pytest` and `httpx`

---

## 🛠️ Project Structure
├── app/
│ ├── main.py # FastAPI application instance
│ ├── models.py # Pydantic models
│ ├── routes.py # API endpoints
│ └── storage.py # In-memory storage (or persistent logic)
├── tests/
│ └── demo_todo.py # Sample test flow using HTTPX
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Installation & Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/fastapi-todo.git
cd fastapi-todo

2. Create a virtual environment (optional)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Run the FastAPI server

uvicorn app.main:app --reload

5. Open your browser:

Visit: http://127.0.0.1:8000/docs for Swagger UI.


🧪 Running Tests


python tests/demo_todo.py