#!/bin/python

# This is an implementation of the stack and queue data structures and their associated operations.

class DoublyLinkedList:

    class Node:

        def __init__(self, value):
            self.next_node = None
            self.prev_node = None
            self.value = value

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def add_front(self, value):
        self.head.next_node = Node(value)
        self.head.next_node.prev_node = self.head
        self.head = self.head.next_node
        size += 1

    def add_back(self, value):
        self.tail.prev_node = Node(value)
        self.tail.prev_node.next_node = self.tail
        self.tail = self.tail.prev_node
        size += 1

    def pop_front(self):
        head = self.head
        head.prev_node.next_node = None
        size -= 1
        return head.value

    def pop_back(self):
        tail = self.tail.value
        tail.next_node.prev_node = None
        size -= 1
        return tail.value

    def __len__(self):
        return size

class Stack:
    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def push(self, item):
        self.linked_list.add_front(item)

    def pop(self):
        return self.linked_list.pop_front()

    def __len__(self):
        return len(self.linked_list)

class Queue:
    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def enqeue(self, item):
        self.linked_list.add_front(item)
        
    def deque(self):
        return self.linked_list.pop_back()

    def __len__(self):
        return len(self.linked_list)


# Stack tests

sequence = [1,2,3,4,5,6]
print "The original sequence:", sequence

stack = Stack()
for n in sequence:
    stack.push(n)

print "A stack is First In First Out, and reverse the item order:"
for n in range(len(stack)):
    print stack.pop()

# Queue tests

queue = Queue()
for n in sequence:
    queue.enqeue(n)

print "A queue is First In Last Out, and maintains item order:"
for n in range(len(queue)):
    print queue.deque()
