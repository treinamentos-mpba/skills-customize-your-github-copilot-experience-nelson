# 📘 Assignment: Building REST APIs with FastAPI framework

## 🎯 Objective

Build a REST API with FastAPI to manage tasks in memory. Practice defining endpoints, handling request and response data, validating input, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create the FastAPI app and list tasks

#### Description
Install `fastapi` and `uvicorn` with `python -m pip install fastapi uvicorn`, then complete the starter code to create a FastAPI application and add endpoints for a health check and listing tasks.

#### Requirements
The completed program must:

- Create a FastAPI app that can be run with `uvicorn starter-code:app --reload`.
- Return a success message from `GET /`.
- Return the current tasks as a JSON list from `GET /tasks`.
- Return an empty list from `GET /tasks` when no tasks have been added.

### 🛠️ Create and retrieve tasks

#### Description
Add the ability to create a task and retrieve a task by its ID. Store tasks in an in-memory collection; a database is not required.

#### Requirements
The completed program must:

- Accept a task title and an optional `completed` value when creating a task with `POST /tasks`.
- Assign each new task a unique integer ID and default `completed` to `false`.
- Return the created task with HTTP status code `201`.
- Return a task by ID from `GET /tasks/{task_id}`.
- Return HTTP status code `404` when the requested task does not exist.

### 🛠️ Update and delete tasks

#### Description
Complete the task management API by implementing update and delete endpoints, and ensure invalid task data is rejected.

#### Requirements
The completed program must:

- Update a task with `PUT /tasks/{task_id}` and return the updated task.
- Delete a task with `DELETE /tasks/{task_id}` and return HTTP status code `204` when successful.
- Return HTTP status code `404` when attempting to update or delete a task that does not exist.
- Reject a task with an empty title using request validation.
- Expose the endpoints in FastAPI's interactive documentation at `/docs`.
