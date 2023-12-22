# Coding Ninjas - Left Rotate an Array by One
from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    new = []
    first = arr[0]
    for i in range(1,n):
        if i < n:
            new.append(arr[i])
        else:
            new.append(arr[n])
    new.append(arr[0])
    return new
