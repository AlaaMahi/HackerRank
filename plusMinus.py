#!/bin/python3

import math
import os
import random
import re
import sys
import functools
from collections import Counter

def plusMinus(arr):
    sign = functools.partial(math.copysign, 1)
    res = map(lambda x: sign(x) if x!=0 else 0, arr)
    cnt = Counter(res)
    print(cnt[1]/len(arr))
    print(cnt[-1]/len(arr))
    print(cnt[0]/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
