#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    curr_ptr = next_ptr = head
    insert_flag = True # flag to check if the data is not inserted. False, if the node is inserted.
    # check if the LL is not empty
    if next_ptr:
        next_ptr = next_ptr.next
        while next_ptr and insert_flag:
            if data < curr_ptr.data: # insert data at first position.
                print('Going here, ', curr_ptr.data,' , ', data)
                node.prev = curr_ptr.prev
                node.next = curr_ptr
                curr_ptr.prev = node
                head = node
                insert_flag = False
            elif next_ptr.data > data and data >= curr_ptr.data: # insert node in between Linked list.
                node.next = curr_ptr.next
                node.prev = next_ptr.prev
                curr_ptr.next = node
                next_ptr.prev = node
                insert_flag = False
            next_ptr = next_ptr.next 
            curr_ptr = curr_ptr.next
        
        if insert_flag: # insert the new node at the end of linked list.
            node.next = next_ptr
            node.prev = curr_ptr
            curr_ptr.next = node
    else: # if the list is empty.
        node.next = None
        node.prev = head
        head = node
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
