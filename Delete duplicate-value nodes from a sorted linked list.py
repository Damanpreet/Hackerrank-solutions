#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    # node_list = []
    
    # nptr = head
    # if nptr:
    #     while nptr:
    #         node_list.append(nptr.data)
    #         nptr = nptr.next
        
    #     nlist = list(set(node_list))
        
    ptr = prev_ptr = head
    
    if ptr:
        ptr = ptr.next
        while ptr:
            print('Main loop:  ---', ptr.data, ' ', prev_ptr.data)
            if ptr.data != prev_ptr.data:
                prev_ptr = prev_ptr.next
                ptr = ptr.next
            else:
                while ptr.data == prev_ptr.data:
                    ptr = ptr.next
                    if ptr is None:
                        break

                prev_ptr.next = ptr
            
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
