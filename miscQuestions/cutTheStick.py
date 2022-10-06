#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMin(arr):
    minE = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minE:
            minE = arr[i]
    # print(minE)
    return minE


def cutTheSticks(arr):
    i, j = 0, 0
    res = []
    lenA1 = len(arr)
    while lenA1 != 0:
        lenA = len(arr)
        print(len(arr))
        # res.append(len(arr))
        small = getMin(arr)
        j = 0
        while j < lenA:
            if arr[j] == small:
                arr.pop(j)
            else:
                arr[j] -= small
                j += 1
            lenA = len(arr)
        # break
        lenA1 = len(arr)
        # print(arr)

        # break
    # return res


if __name__ == '__main__':

    n = 6

    arr = [5, 4, 4, 2, 2, 8]

    result = cutTheSticks(arr)

    print(result)
