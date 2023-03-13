#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest_int = 0
    list_len = len(my_list)

    if list_len == 0:
        return None
    else:
        for i in range(list_len):
            if my_list[i] > biggest_int:
                biggest_int = my_list[i]
        return biggest_int
