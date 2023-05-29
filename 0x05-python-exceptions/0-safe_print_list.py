#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elements = 0
    for element in my_list[:x]:
        try:
            print("{}".format(element), end='')
            num_elements += 1
        except Exception:
            continue

    print("")

    return num_elements
