#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = len(sys.argv) - 1
    if num == 1:
        print("{} argument:".format(num))
    elif num == 0:
        print("{} arguments.".format(num))
    else
        print("{} arguments:".format(num))
    for i in range(num):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
