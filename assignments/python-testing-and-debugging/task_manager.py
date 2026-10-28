def add_task(tasks, title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False,
    }
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


def find_task(tasks, title):
    for task in tasks:
        if task["title"] == title:
            return task
    return None
