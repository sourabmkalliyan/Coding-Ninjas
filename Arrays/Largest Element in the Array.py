from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    arr.sort()
    arr.reverse()
    return arr[0]
    pass
