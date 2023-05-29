#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_elements = 0
    for element in my_list[:x]:
        try:
            print("{:d}".format(element), end='')
            num_elements += 1
        except (ValueError, TypeError):
            pass

    print("")

    return num_elements
