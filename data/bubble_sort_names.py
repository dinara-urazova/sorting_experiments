from time import time
from typing import Callable



def bubble_sort (arr: list[int], compare_fn) -> tuple[float, int]:
    n = len(arr)
    comparison_count = 0
    start_time = time()
    for i in range(n-1):
        for j in range(n-1-i):
            comparison_count +=1
            compare_result = compare_fn(arr[j], arr[j+1])
            if compare_result > 0:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    finish_time = time()
    sorting_time = finish_time - start_time

    return (sorting_time, comparison_count)


def cmp_numbers(a: int, b: int)-> int:
    return a - b

def cmp_names(person1: dict, person2: dict)-> int:
    if person1['surname'] != person2['surname']:
        return -1 if person1['surname'] < person2['surname'] else 1
    return -1 if person1['name'] < person2['name'] else 1



arrNumbers = [0,5,3,7,8,1]
arrNames = [
    {
        "surname": 'Иванов',
        "name" : 'Иван'
    },

    {
        "surname": "Иванов",
        "name" : "Артем"
    },

    {
        "surname": "Артамонов",
        "name" : "Савелий"
    },
]


print(arrNumbers)

print(arrNumbers)
print(bubble_sort(arrNumbers, cmp_numbers))
# print(arrNames)
# print(bubble_sort(arrNames, cmp_names))
# print(arrNames)