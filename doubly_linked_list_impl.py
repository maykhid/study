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


def sortedInsert(head, data):
    temp=DoublyLinkedListNode(data)
    if head==None: 
        head=temp
    else:
        cur=head
        if cur.data>=data:  #insert temp to head
            temp.next=cur
            cur.prev=temp
            return temp
        else:  #insert temp to non-head part of list
            while cur.next!=None:
                if cur.data<data and cur.next.data>=data:
                    temp.next=cur.next  
                    cur.next.prev=temp  
                    cur.next=temp
                    temp.prev=cur    
                    break
                else: 
                    cur=cur.next
            else: 
                cur.next=temp
                temp.prev=cur  
    return head

print(sortedInsert(DoublyLinkedListNode(1), 5))