#!/bin/python3

import math
import os
import random
import re
import sys

class Stack:
    def __init__(self):
        self.bracket_list = []
    
    def push(self, item):
        self.bracket_list.append(item)
    
    def pop(self, item):
        if len(self.bracket_list) != 0:
            if (item == ')' and self.bracket_list[-1] == '(') or (item == ']' and self.bracket_list[-1] == '[') or (item == '}' and self.bracket_list[-1] == '{'):
                self.bracket_list.pop()
                return 0
            else:
                return 1
        else:
            return 1

    def isEmpty(self):
        if len(self.bracket_list) == 0:
            return True
        else:
            return False

# Complete the isBalanced function below.
def isBalanced(s):
    st = Stack()
    for bracket in s:
        if bracket in ['(','{','[']:
            st.push(bracket)
        else:
            ret_value = st.pop(bracket)
            if ret_value == 1:
                return 'NO'

    if st.isEmpty():
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
