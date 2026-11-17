
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI application
app = FastAPI()

# Temporary storage for todo list
todo_list = []

# todo list schema enforcer through pydantic
class Todo(BaseModel):
    title: str
    description: str = None
    completed: bool = False


# todo list home point
@app.get("/")
def home():
    return {"message": "Welcome to todo List Home Page"}


# 2. Create a todo item
@app.post("/add-todo")
def add_task(task: Todo):
    new_task = {
        "id": len(todo_list) + 1,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    todo_list.append(new_task)

    return {
        "message": "Todo list updated",
        "task": new_task
    }


# 3. Get request fro whole todo list
@app.get("/todo-list")
def get_all_tasks():
    return {
        "total_tasks": len(todo_list),
        "tasks": todo_list
    }


# 4. Get request for specific todo task
@app.get("/todo-list/{todo_id}")
def get_task(todo_id: int):

    for task in todo_list:
        if task["id"] == todo_id:
            return task

    return {"Todo item request invalid"}


# 5. Update a task
@app.put("/todo-list/{task_id}")
def update_task(task_id: int, updated_task: Todo):

    for task in todo_list:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed
            return {
                "message": "Task updated successfully",
                "task": task
            }



# 6. Delete a task
@app.delete("/todo-list/{task_id}")
def delete_task(task_id: int):

    for task in todo_list:
        if task["id"] == task_id:
            todo_list.remove(task)
            return {
                "message": "Task deleted successfully"
            }
    return {"Delete request invalid as id invalid"}