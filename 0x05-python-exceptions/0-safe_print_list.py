#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''
    This function prints x elemts of a list
    Args:
        my_list(list): The list's elemnts to be printed
        x (int): num of elements
    Returns:
        The num of elemts printed
    '''
    i = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j], end="")
            i += 1
        except IndexError:
            break
     print("")
     return i
