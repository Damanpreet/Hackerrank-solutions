#!/bin/python3

import os
import sys


class Stack:
    def __init__(self):
        self.cylinders = []
    
    def push(self, item):
        self.cylinders.append(item)

    def pop(self):
        if len(self.cylinders) != 0:
            item = self.cylinders.pop()
            return item

    def find_length(self):
        return sum(self.cylinders)

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    # h1 = h2 = h3 = Stack()
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()
    length_list = []

    for item in reversed(h1):
        s1.push(item)

    for item in reversed(h2):
        s2.push(item)

    for item in reversed(h3):
        s3.push(item)

    sum1 = s1.find_length()
    sum2 = s2.find_length()
    sum3 = s3.find_length()
    if sum1 == sum2 == sum3 :
        return sum1

    while sum1 != sum2 or sum1 != sum2 or sum2 != sum3:
        if sum1 > sum2 or sum1 > sum3:
            sum1 -= s1.pop()
        
        if sum2 > sum1 or sum2 > sum3:
            sum2 -= s2.pop()
        
        if sum3 > sum1 or sum3 > sum2:
            sum3 -= s3.pop()
        
    return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
