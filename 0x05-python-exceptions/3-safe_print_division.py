#!/usr/bin/python3
def safe_print_division(a, b):
    '''Returns a/b'''
    try:
        divErr = a / b
    except ZeroDivisionError:
        divErr = None
    finally:
        print("Inside result: {}".format(divErr))
    return divErr
