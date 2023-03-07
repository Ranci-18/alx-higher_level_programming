#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            offset_value = 32
        else:
            offset_value = 0
        print("{:c}".format(ord(str[i]) - offset_value), end='')
    print()
