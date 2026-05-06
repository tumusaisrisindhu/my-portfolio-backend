todos = []
current_id = 1


def get_all_todos():
    return todos


def create_todo(data):
    global current_id

    todo = {
        "id": current_id,
        "title": data["title"],
        "items": data["items"],  # list of { text, completed }
    }

    todos.append(todo)
    current_id += 1

    return todo


def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]


def update_todo(todo_id, data):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = data["title"]
            todo["items"] = data["items"]
            return todo

    return None