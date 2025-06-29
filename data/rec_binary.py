def binary_search(array, left, right, x):
    if left > right:
        return -1
    elif left <= right:
        mid = (left+right)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, left, mid-1, x)
        elif array[mid] < x:
            return binary_search(array,mid+1,right,x)
    return -1
array = [2,5,6,8,11,15,22,35,67,85,86,91,99,100,101,123,125,130]
x = 99
right = len(array)-1
left = 0
index = binary_search(array,left,right,x)
if index != -1:
    print(f"The value {x} is on position {index}")
else:
    print(f"No value {x} in the array")