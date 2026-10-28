from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def health_check():
    # TODO: Return a JSON message indicating that the API is running.
    pass


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks as a list.
    pass


# TODO: Add POST /tasks to create a task.
# TODO: Add GET /tasks/{task_id} to retrieve a task or return HTTP 404.
# TODO: Add PUT /tasks/{task_id} to update a task or return HTTP 404.
# TODO: Add DELETE /tasks/{task_id} to delete a task or return HTTP 404.
