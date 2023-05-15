def print_list_integer(my_list=None):
    """Prints all the integers of a list.

    Args:
        my_list (list, optional): The list of integers. Defaults to None.

    """
    if my_list is None:
        my_list = []

    for i in my_list:
        if isinstance(i, int):
            print("{:d}".format(i))
        else:
            print("Error: List contains non-integer values.")
