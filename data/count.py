from time import time

def input_data() ->list[int]:
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))

    return array
        

def map_value_to_counter_index (x: int, min_value: int) -> int:
    return x - min_value

def map_counter_index_to_value (x: int, min_value: int) -> int:
    return x + min_value


def get_stat(array:list[int]) -> tuple[int, int]:
    max_value = array[0]
    min_value = array[0]

    for i in range(1,len(array)):
        if array[i] < min_value:
            min_value = array[i]
        if array[i] > max_value:
            max_value = array[i]
    return (min_value, max_value-min_value+1)


def counting_sort(array: list[int]) -> tuple[float, int]:
    start_time = time()
    (min_value, r) = get_stat(array) 
    
    counter = [0] * r
    
    for i in range(len(array)):
        counter_index = map_value_to_counter_index(array[i], min_value)
        counter[counter_index] +=1

    i = 0
    insert_count = 0
    for counter_index in range(len(counter)):
        value= map_counter_index_to_value(counter_index, min_value)
        frequency = counter[counter_index]
        for j in range(frequency):  
            insert_count +=1     
            array[i] = value
            i +=1
    finish_time  = time()
    sorting_time = finish_time - start_time

    return (sorting_time, insert_count)

def output_data(array:list[int], sorting_time: float)  -> None:
    n = len(array)

    print(n)
    print(sorting_time)
    
    for i in range(n):
        print(array[i])




array = input_data()
(sorting_time, insert_count) = counting_sort(array)
output_data(array, sorting_time)