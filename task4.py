import sys
import math

def prnt(arg, result):
    print("ln({0}) is {1}".format(arg, "incorrect" if result == -1 else result))

def version1():
    for arg in sys.argv[1:]:
        result = -1
        try:
            result = math.log(float(arg))
        except ValueError:
            pass
        prnt(arg, result)


def version2():
    for i in range(1, len(sys.argv)):
        result = -1
        try:
            result = math.log(float(sys.argv[i]))
        except ValueError:
            pass
        prnt(sys.argv[i], result)
        i += 1

def version3():
    i = 1
    while i < len(sys.argv):
        result = -1
        try:
            result = math.log(float(sys.argv[i]))
        except ValueError:
            pass
        prnt(sys.argv[i], result)
        i += 1

def version4():
    i = 1
    while True:
        result = -1
        try:
            result = math.log(float(sys.argv[i]))
        except ValueError:
            pass
        except IndexError:
            break
        prnt(sys.argv[i], result)
        i += 1

