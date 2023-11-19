""" Functions module used in the main code."""

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads a text file and returns a list."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write a list into a text file."""
    with open(filepath,'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    """ The __name__ variable is only equal to main
    when this script (functions) is being run on its own.
    Therefore this condition is only True if we run this
    specific script (not through another script)! """
    print("hello")
    print(get_todos())