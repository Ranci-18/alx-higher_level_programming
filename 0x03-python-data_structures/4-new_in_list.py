#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    my_list_length = len(my_list)
    if idx > my_list_length - 1:
        return my_list

    if 0 <= idx <= my_list_length - 1:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
