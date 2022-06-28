#!/usr/bin/python3
<<<<<<< HEAD
def safe_print_list_integers(my_list=[], x=0):
    cmpt = 0
    for index in range(x):
        try:
            print('{:d}'.format(my_list[index]), end='')
            cmpt += 1
        except IndexError:
            break
        except Exception:
            pass

    print('')
    return cmpt
=======
# 2-safe_print_list_integers.py
# this is my code

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
>>>>>>> 2b46e3436182605e0307de25f4915b222a5ded69
