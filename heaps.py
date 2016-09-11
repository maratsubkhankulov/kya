#!/bin/python

import math

def swap(A, a, b):
    tmp = A[a]
    A[a] = A[b]
    A[b] = tmp

# Min heap

def is_min_heap(heap):
    def helper(heap, parent):
        if parent > len(heap) - 1:
            return True

        left = 2*parent + 1
        right = 2*parent + 2

        if left < len(heap) and heap[left] < heap[parent]:
            return False
        if right < len(heap) and heap[right] < heap[parent]:
            return False

        return helper(heap, left) and helper(heap, right)

    return helper(heap, 0)

def down_heap_min(A, i):
    left = 2*i + 1
    right = 2*i + 2
    smallest = i

    if left < len(A) and A[left] < A[smallest]:
        smallest = left
    if right < len(A) and A[right] < A[smallest]:
        smallest = right

    if not smallest == i:
        swap(A, i, smallest)
        down_heap_min(A, smallest)

def up_heap_min(A, i):
    if i == 0:
        return
    parent = int(math.floor((i - 1)/2.0))

    if A[i] < A[parent]:
        swap(A, i, parent)       
        up_heap_min(A, parent)

def build_heap_min(array):
    half_length = int(math.floor(len(array)/2.0))
    
    for i in range(half_length, -1, -1):
        down_heap_min(array, i)
    return array

def extract_min(heap):
    if len(heap) > 1:
        first = heap[0]
        last = heap.pop()
        heap[0] = last
        down_heap_min(heap, 0)
        return first
    else:
        return heap.pop()

def insert_min(heap, value):
    heap.append(value)
    last = len(heap) - 1
    up_heap_min(heap, last)

# Max heap

def is_max_heap(heap):
    def helper(heap, parent):
        if parent > len(heap) - 1:
            return True

        left = 2*parent + 1
        right = 2*parent + 2

        if left < len(heap) and heap[left] > heap[parent]:
            print heap[left], heap[parent]
            return False
        if right < len(heap) and heap[right] > heap[parent]:
            print heap[right], heap[parent]
            return False

        return helper(heap, left) and helper(heap, right)

    return helper(heap, 0)

def down_heap_max(A, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right

    if not largest == i:
        swap(A, i, largest)
        down_heap_max(A, largest)

def up_heap_max(A, i):
    if i == 0:
        return
    parent = int(math.floor((i - 1)/2.0))

    if A[i] > A[parent]:
        swap(A, i, parent)       
        up_heap_max(A, parent)

def build_heap_max(heap):
    half_length = int(math.floor(len(heap)/2.0))
    for i in range(half_length, -1, -1):
        down_heap_max(heap, i)
    return heap

def extract_max(heap):
    if len(heap) > 1:
        first = heap[0]
        last = heap.pop()
        heap[0] = last
        down_heap_max(heap, 0)
        return first
    else:
        return heap.pop()

def insert_max(heap, value):
    heap.append(value)
    last = len(heap) - 1
    up_heap_max(heap, last)

# Tests

# Build heap
print("Test build_heap_max")
heap = build_heap_max([1,2,3,4,5,61,2])
print "Test 1:", heap, is_max_heap(heap)
heap = build_heap_max([3,6,7,4,5])
print "Test 2:", heap, is_max_heap(heap)

print("Test build_heap_min")
heap = build_heap_min([1,2,3,4,5,61,2])
print "Test 1:", heap, is_min_heap(heap)
heap = build_heap_min([3,6,7,4,5])
print "Test 2:", heap, is_min_heap(heap)

# Extract
input_list = [1,2,3,4,5,61,2]
heap = build_heap_min(input_list[:])
extracted = []
input_list.sort()
length = len(heap)
for n in range(length):
    extracted.append(extract_min(heap))
result = extracted == input_list
print "Test extract_min: ", extracted, input_list, result

input_list = [1,2,3,4,5,61,2]
heap = build_heap_max(input_list[:])
extracted = []
length = len(heap)
input_list.sort(reverse=True)
for n in range(length):
    extracted.append(extract_max(heap))
result = extracted == input_list
print "Test extract_max: ", extracted, input_list, result

# Insert
inserted = []
input_list = [2,61,5,4,3,2,1]
for n in input_list:
    insert_min(inserted, n)
heap = build_heap_min(input_list[:])
result = inserted == heap
print "Test insert_min: ", inserted, heap, result

inserted = []
input_list = [2,61,5,4,3,2,1]
for n in input_list:
    insert_max(inserted, n)
heap = build_heap_max(input_list[:])
result = inserted == heap
print "Test insert_max: ", inserted, heap, result
