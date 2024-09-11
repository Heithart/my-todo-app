FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read the text file and returns 
        the list of ToDo items 
    """
    with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a TDo items list
        into the doc
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)