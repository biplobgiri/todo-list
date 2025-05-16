import httpx

BASE_URL = "http://127.0.0.1:8000"

def add_todo(title, description):
    response = httpx.post(f"{BASE_URL}/todo/", json={
        "title": title,
        "description": description
    })
    result = response.json()
    print("✅ Added:", result)
    return result["id"]  

def get_todos():
    response = httpx.get(f"{BASE_URL}/todo/")
    todos = response.json()
    print("📋 Current Todos:", todos)
    return todos

def delete_todo(todo_id):
    response = httpx.delete(f"{BASE_URL}/todo/{todo_id}")
    result = response.json()
    print("❌ Deleted:", result)
    return result

if __name__ == "__main__":
    httpx.delete(f"{BASE_URL}/todo/clear") 
    
    id1 = add_todo("Fusemachines", "Finish assignment")
    id2 = add_todo("movies", "buy the tickets")
    
    todos = get_todos()
    
    if todos:
        first_id = todos[0]["id"]
        delete_todo(first_id)
  
    get_todos()