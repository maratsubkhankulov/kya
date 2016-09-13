#!/bin/python

# This is an implementation of the stack and queue data
# structures and their associated operations.

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
        if self.size == 0:
            self.head = self.Node(value)
            self.tail = self.head
        else:
            self.head.next_node = self.Node(value)
            self.head.next_node.prev_node = self.head
            self.head = self.head.next_node
        self.size += 1

    def add_back(self, value):
        if self.size == 0:
            self.head = self.Node(value)
            self.tail = self.head
        else:
            self.tail.prev_node = Node(value)
            self.tail.prev_node.next_node = self.tail
            self.tail = self.tail.prev_node
        self.size += 1

    def pop_front(self):
        value = self.head.value
        self.head = self.head.prev_node
        if self.head:
            self.head.next_node = None
        self.size -= 1
        return value

    def pop_back(self):
        value = self.tail.value
        self.tail = self.tail.next_node
        if self.tail:
            self.tail.prev_node = None
        self.size -= 1
        return value

    def __len__(self):
        return self.size

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
        
    def dequeue(self):
        return self.linked_list.pop_back()

    def __len__(self):
        return len(self.linked_list)


# Stack test

sequence = [1,2,3,4,5,6]
print "The original sequence:", sequence

stack = Stack()
print "A stack is First In First Out, and reverses the item order:"

for n in sequence:
    print "push(%i)" % n
    stack.push(n)
for n in range(len(stack)):
    print "pop() ->", stack.pop()

# Queue test

queue = Queue()
print "A queue is First In Last Out, and maintains item order:"

for n in sequence:
    print "enqueue(%i)" % n
    queue.enqeue(n)
for n in range(len(queue)):
    print "dequeue() ->", queue.dequeue()
