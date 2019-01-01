#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    pos = 0
    jump_count = 0
    while pos < len(c)-1:
        pos = pos+2 if len(c) - pos -1 >= 2 else pos+1
        if c[pos] == 1:
            pos -= 1
        jump_count += 1
    

    return jump_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
