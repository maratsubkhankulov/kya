#!/bin/python

def search(Arr, item):
    if len(Arr) == 0:
        return -1

    left = 0
    right = len(Arr) 

    if item < Arr[left] or item > Arr[right - 1]:
        return - 1

    while (right - left) > 1:
        center = right - (right-left)/2
        if item < Arr[center]:
            right = center
        elif item > Arr[center]:
            left = center 
        else:
            return center

    if (right - left) == 1:
        if item == Arr[left]:
            return left

    return -1

def test_sorted(Arr):
    if len(Arr) < 2:
        return True

    ii = 1
    while ii < len(Arr):
        if Arr[ii-1] > Arr[ii]:
            return False
        ii = ii + 1
    return True

def test_search():

    print "Test 1:", search([1], 1) == 0
    print "Test 2:", search([1,2], 2) == 1
    print "Test 3:", search([1,2,3], 2) == 1
    print "Test 4:", search([1,2,3], 5) == -1
    print "Test 5:", search([1,2,3], -5) == -1
    print "Test 6:", search([1,2,5], 3) == -1
    print "Test 7:", search([1,2,3,4], 4) == 3
    print "Test 8:", search([1,2,3,4], 1) == 0
    print "Test 8:", search([1,2,3,4], 1) == 0
    print "Test 9:", search([1,2,2,2,2], 2) == 3

if __name__ == "__main__":
    test_search()
