#!/usr/bin/python3
for j in range(90, 64, -1):
    if j % 2 == 0:
        print("{:c}".format(j).lower(), end="")
    else:
        print("{:c}".format(j), end="")
