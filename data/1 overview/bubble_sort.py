from time import time
from typing import Callable

# Ввод данных
def input_data() -> list[int]:
    n = int(input())
    nums = list()
    for _ in range(n):  
        nums.append (int(input()))
    return nums

# Сортировка
def bubble_sort (nums: list[int], compare_fn: Callable[[int, int], int]) -> tuple[float, int]:

    n = len(nums)
    comparison_count = 0
    start_time = time()
    for i in range(n-1):
        for j in range(n-1-i):
            comparison_count +=1
            compare_result = compare_fn(nums[j], nums[j+1])
            if compare_result > 0:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    finish_time = time()
    sorting_time = finish_time - start_time

    return (sorting_time, comparison_count)

# Вывод данных
def output(nums: list[int], sorting_time: float, comparison_count: int) -> None:
    n = len(nums)
    print (sorting_time) 
    print (comparison_count)
    print (n)
    
    for i in range (n):
        print(nums[i])
        
def compare_increase(a: int, b: int) -> bool:
    return a - b


def compare_decrease(a: int, b: int) -> bool:
    return b - a
   

nums = input_data()  # return nums from local frame to main frame (присваивание)
(sorting_time, comparison_count) = bubble_sort(nums, compare_increase)  

output(nums, sorting_time, comparison_count)