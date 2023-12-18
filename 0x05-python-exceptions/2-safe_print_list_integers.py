#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            if isinstance(int, my_list[i]):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except Exception:
        return
    else:
        print()
        return count
