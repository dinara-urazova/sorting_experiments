from time import time


def input_data() -> list[int]:
    n = int(input())
    array = list()
    for i in range(n):  
        array.append (int(input()))
    return array


    
def list_sort(array: list[int]) -> float:
    start_time = time()
    
    array.sort()  
            
    finish_time = time()
    sorting_time = finish_time - start_time   
    
    return sorting_time



def output(array: list[int], sorting_time: float) -> None:
    n = len(array)
    print (sorting_time)
    print (n)
 
    
    
    for i in range (n):
        print(array[i])    


array = input_data()
sorting_time = list_sort(array)
output(array, sorting_time)



