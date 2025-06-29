from time import time


def input_data() -> list[int]:
    n = int(input())
    arr = list()
    for i in range(n):  
        arr.append (int(input()))
    return arr



def selection_search(arr, n) -> int:
    compare_count = 0
    for i in range(n-1):
        smallest = i
        for j in range(i+1, n):
            compare_count += 1
            if array[j] < array[smallest]:
                array[j], array[smallest] = array[smallest], array[j]  # swap elements if the next element is bigger than the current "smallest"
    return compare_count



def output(arr: list[int], sorting_time: float, compare_count: int) -> None:
    n = len(arr)
    print (sorting_time)
    print (compare_count) 
    print (n)
    
    for i in range (n):
        print(arr[i])


array = input_data()
start_time = time()
compare_count = selection_search(array, len(array))
finish_time = time()
sorting_time  = finish_time - start_time
output(array, sorting_time, compare_count)

