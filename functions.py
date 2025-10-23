# Function to get todos from a file
def get_todos(file_path = "todos.txt"): #param file_path
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

# Function to write todos to a file
def write_todos(todos_arg , file_path="todos.txt"):
    with open(file_path, "w") as file:
        file.writelines(todos_arg)



