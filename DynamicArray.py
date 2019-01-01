#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    g = globals()
    lastAns = []
    for i in range(n):
        g['S{0}'.format(i)] = []
    lastAnswer = 0
    for q in queries:
        if q[0] == 1:
            seq_no = (q[1]^lastAnswer)%n
            g['S{0}'.format(seq_no)].append(q[2])
        else:
            seq_no = (q[1]^lastAnswer)%n
            index_no = q[2] % len(g['S{0}'.format(seq_no)])
            lastAnswer = g['S{0}'.format(seq_no)][index_no]
            lastAns.append(lastAnswer)
    return lastAns

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
