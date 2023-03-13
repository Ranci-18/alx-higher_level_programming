#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        el0_a = 0
        el1_a = 0
    elif len_a == 1:
        el0_a = tuple_a[0]
        el1_a = 0
    else:
        el0_a = tuple_a[0]
        el1_a = tuple_a[1]

    if len_b == 0:
        el0_b = 0
        el1_b = 0
    elif len_b == 1:
        el0_b = tuple_b[0]
        el1_b = 0
    else:
        el0_b = tuple_b[0]
        el1_b = tuple_b[1]

    tuple_c = (el0_a + el0_b, el1_a + el1_b)
    return tuple_c
