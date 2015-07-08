import sys
import math

def version1():
    for arg in sys.argv[1:]:
        result = -1
        try:
            result = math.log(float(arg))
        except ValueError:
            pass
            print("log({0}) is {1}".format(arg, "incorrect" if result == -1 else result))

