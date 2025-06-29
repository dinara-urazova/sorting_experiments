def binary_search(array,n,x):
    left = 0
    right = n
    while left <= right:
        mid = (left+right)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            right = mid -1
        elif array[mid] < x:
            left = mid + 1
    return "Not found"        


arr = [2,5,6,8,11,15,22,35,67,85,86,91,99,100,101,123,125,130]
n = len(arr)-1    # here we calculate index of the last element
x = 75             
res = binary_search(arr,n,x)
if res != "Not found":
    print(f"The value {x} is on position {res}")
print(f"The value {x} is not in the array.")



