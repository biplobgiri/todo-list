

# 📝 FastAPI Todo App

A simple Todo API built with **FastAPI**. This project allows users to create, read, update, and delete tasks (CRUD). It also includes automated testing using **Pytest** and **GitHub Actions** to ensure code quality.

## 🚀 Features

- ✅ Create todo items
- 📋 View all todos or a specific one by ID
- ✏️ Update existing todos
- ❌ Delete todos
- 🧪 Automated testing with Pytest
- ⚙️ CI/CD pipeline via GitHub Actions

## 📁 Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   ├── routes.py        # API endpoints
│   ├── schemas.py       # Pydantic models
│   └── storage.py       # In-memory todo storage
├── tests/
│   └── test_main.py     # Test cases using pytest
├── .github/
│   └── workflows/
│       └── test.yml     # GitHub Actions workflow
├── .gitignore
├── requirements.txt
└── README.md
```

## 🧪 Running Tests

To run the tests locally:

```bash
pip install -r requirements.txt
pytest -v --disable-warnings
```

## 🚦 GitHub Actions

This project uses GitHub Actions to automatically run tests when a pull request is created targeting the main branch.

The workflow runs on:

```yaml
on:
  pull_request:
    branches:
      - main
```

## 🛠️ Installation and Usage

1. Clone the repository:
```bash
git clone https://github.com/yourusername/todo-list.git
cd todo-list
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI app:
```bash
uvicorn app.main:app --reload
```

4. Visit the interactive API docs at:
```
http://127.0.0.1:8000/docs
```

## 📌 Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- Pytest

## 🙌 Contributing

Pull requests are welcome! Please make sure to write appropriate tests and follow the existing code structure.

## 📄 License

This project is licensed under the MIT License.


