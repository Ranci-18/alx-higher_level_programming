#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for integers in my_list:
        print("{:d}".format(my_list[integers - 1]))
