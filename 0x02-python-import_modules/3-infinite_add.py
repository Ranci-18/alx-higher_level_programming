#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    addition = 0
    if args == 0:
        print("{}".format(addition))
    elif args == 1:
        print("{}".format(int(sys.argv[1])))
    else:
        for i in range(1, args + 1):
            addition += int(sys.argv[i])
        print("{}".format(addition))
