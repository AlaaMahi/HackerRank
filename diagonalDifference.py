#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def diagonalDifference(arr):
    diag0, diag1 = 0, 0
    for i in range(len(arr)):
        if -100 <= arr[i][i] <= 100 and -100 <= arr[i][len(arr)-1-i] <= 100:
            diag0 += arr[i][i]
            diag1 += arr[i][len(arr)-1-i]
    return abs(diag1-diag0)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
