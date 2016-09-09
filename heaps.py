#!/bin/python

import math

# Given an array of ints return a heap

def max_heapify(A, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right

    if not largest == i:
        # swap i and largest
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp

        max_heapify(A, i)

def build_max_heap(array):
    half_length = int(math.floor(len(array)/2.0))
    print half_length
    for i in range(half_length, -1, -1):
        max_heapify(array, i)
    return array

def min_heapify(A, i):
    left = 2*i + 1
    right = 2*i + 2
    smallest = i

    if left < len(A) and A[left] < A[smallest]:
        smallest = left
    if right < len(A) and A[right] < A[smallest]:
        smallest = right

    if not smallest == i:
        # swap i and smallest
        tmp = A[i]
        A[i] = A[smallest]
        A[smallest] = tmp

        min_heapify(A, i)

def build_min_heap(array):
    half_length = int(math.floor(len(array)/2.0))
    
    for i in range(half_length, -1, -1):
        min_heapify(array, i)
    return array

print(build_max_heap([1,2,3,4,5,61,2]))
print(build_max_heap([3,6,7,4,5]))
print(build_min_heap([1,2,3,4,5,61,2]))
print(build_min_heap([3,6,7,4,5]))
