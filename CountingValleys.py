#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    no_valleys = 0
    below_valley = False

    for i in range(n):
        if s[i] == 'U':
            level += 1
        else:
            level -= 1
        
        if below_valley is False and level < 0: 
            no_valleys += 1
            below_valley = True

        if level == 0:
            below_valley = False

    return no_valleys
	
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
