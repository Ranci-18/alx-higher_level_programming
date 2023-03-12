#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx < 0:
            return None
        if i == idx and idx > 0:
            return my_list[i]
