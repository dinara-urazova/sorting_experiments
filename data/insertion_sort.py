from time import time


def input_data() -> list[int]:
    n = int(input())
    arr = list()
    for i in range(n):  
        arr.append (int(input()))
    return arr


def insertion_sort(arr, n) -> int:
    swaps= 0
    for i in range(1, n):
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1]= arr[j]
            j -= 1
            swaps += 1
        arr[j+1] = key
    return swaps


def output(arr: list[int], sorting_time: float, swaps: int) -> None:
    n = len(arr)
    print (sorting_time) 
    print(swaps)
    print (n)
    
    for i in range (n):
        print(arr[i])


arr = input_data()  # return nums from local frame to main frame (присваивание)
start_time = time()
swaps = insertion_sort (arr, len(arr))  
finish_time = time()
sorting_time  = finish_time - start_time
output(arr, sorting_time, swaps)

