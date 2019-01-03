#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    a = list(set(arr))
    max_count = 0
    count_ele = 0
    
    for i in a:
        count_ele = arr.count(i)
        
        if max_count < count_ele:
            max_count = count_ele

    return (len(arr) - max_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
