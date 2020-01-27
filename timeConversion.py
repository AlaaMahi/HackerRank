#!/bin/python3

import os
import sys


def timeConversion(s):
    if s[:2] == '12':
        if 'PM' in s:
            return s[:8]
        else:
            return '00'+s[2:8]
    else:
        if 'PM' in s:
            h = int(s[:2])+12
            return str(h)+s[2:8]
        else:
            return s[:8]
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
