#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key_list = list(a_dictionary.keys())
    high_score = 0
    high_key = None

    for i in key_list:
        if a_dictionary[i] > high_score:
            high_score = a_dictionary[i]
            high_key = i

    return high_key
