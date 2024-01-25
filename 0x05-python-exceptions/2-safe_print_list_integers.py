#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.
    Args:
        my_list (list): The list to print elements from.
        x (int): The num of elems to print.
    Returns:
        The num of elmnts printed.
    """
    i = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            i += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (i)

