#!/usr/bin/python3
def number_keys(a_dictionary):
    keys = list(a_dictionary.keys())
    count_keys = 0

    for i in keys:
        count_keys += 1
    return count_keys
