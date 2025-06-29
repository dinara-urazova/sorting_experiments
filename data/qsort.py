from time import time


def input_data() -> list[int]:
    n = int(input())
    arr = list()
    for i in range(n):  
        arr.append (int(input()))
    return arr

def qsort(arr: list[int], start: int, finish: int) -> None:
    i = start
    j = finish
    pivot = arr[(i+j)//2]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while pivot < arr[j]:
            j -= 1
        if i <= j:
            (arr[i], arr[j]) = (arr[j], arr[i])
            i += 1
            j -= 1
    if start < j:
        qsort(arr, start, j)
    if i < finish:
        qsort(arr, i, finish)
  


def output(arr: list[int], sorting_time: float) -> None:
    n = len(arr)
    print (sorting_time) 
    print (n)
    
    for i in range (n):
        print(arr[i])


arr = input_data()  # return nums from local frame to main frame (присваивание)
start_time = time()
qsort(arr, 0, len(arr)-1)  
finish_time = time()
sorting_time  = finish_time - start_time
output(arr, sorting_time)

