# Recursive implementation of the binary search algorithm
def binarySearch(arr, left, right, number):
 
    # The starting point (search space is exhausted).
    if left > right:
        return -1
 
    # Discovers the mid-point in the search space and compares it to the target
    mid = (left + right) // 2
 
    # Overflow can happen. Use below
    # mid = left + (right-left) / 2
 
    # Base condition (a target is found)
    if number == arr[mid]:
        return mid
 
    # Remove all elements from the right search space, including the middle element.
    elif number < arr[mid]:
        return binarySearch(arr, left, mid - 1, number)
 
    # Remove all elements from the left search space, including the middle element.
    else:
        return binarySearch(arr, mid + 1, right, number) 
 
arr = []
n = int(input('Enter the value of array size '))
for i in range(0,n):
    temp = int(input('Enter array value '))
    arr.append(temp)
number = int(input('Enter the target value '))
 
(left, right) = (0, len(arr) - 1)
index = binarySearch(arr, left, right, number)
 
if index != -1:
    print('Element found at index', index)
else:
    print('Element not found in the array')