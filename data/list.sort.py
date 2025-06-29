from time import time
from functools import cmp_to_key
counter = 0

def input_data() -> list[int]:
    n = int(input())
    array = list()
    for i in range(n):  
        array.append (int(input()))
    return array

def compare_fn(a: int, b: int) -> float:
    global counter
    counter += 1
    return a - b    # ниже развернутый вариант этой строки
    # if a < b:
    #     return -1
    # if a > b:
    #     return 1
    # return 0

    
def list_sort(array: list[int]) -> float:
    start_time = time()
    
    array.sort(key = cmp_to_key(compare_fn))  
            
    finish_time = time()
    sorting_time = finish_time - start_time   
    
    return sorting_time



def output(array: list[int], sorting_time: float) -> None:
    n = len(array)
    print (sorting_time)
    print (n)
    print (counter)
    
    
    for i in range (n):
        print(array[i])    


array = input_data()
sorting_time = list_sort(array)
output(array, sorting_time)



