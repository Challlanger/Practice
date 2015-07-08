import sys
import math


def version1():
    for arg in sys.argv[1:]:
        result = -1
        try:
            result = math.log(float(arg))
        except ValueError:
            pass
        print("ln({0}) is {1}".format(arg, "incorrect" if result == -1 else result))


def version2():
    for i in range(1, len(sys.argv)):
        result = -1
        try:
            result = math.log(float(sys.argv[i]))
        except ValueError:
            pass
        print("ln({0}) is {1}".format(sys.argv[1], "incorrect" if result == -1 else result))
        i += 1
