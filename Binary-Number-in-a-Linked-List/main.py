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



#
# Complete the 'getNumber' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_SINGLY_LINKED_LIST binary as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNumber(binary):
    cur = binary
    elems = []
    while cur:
        elems.append(cur.data)
        cur = cur.next
    
    i = 0
    res = 0
    lenth = len(elems) - 1
    
    while lenth >= 0:
        if elems[lenth] == 1:
            res += pow(2, i)
        lenth -= 1
        i += 1
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    binary_count = int(input().strip())

    binary = SinglyLinkedList()

    for _ in range(binary_count):
        binary_item = int(input().strip())
        binary.insert_node(binary_item)

    result = getNumber(binary.head)

    fptr.write(str(result) + '\n')

    fptr.close()
