from sys import argv
from time import time


def fib(num):
    global cache
    if cache[num] != None:
        return cache[num]
    cache[num] = num if num <= 1 else fib(num-1) + fib(num-2)
    return cache[num]

n = int(argv[1])
cache = [None] * (n+1)

start_time = time()
result = fib(n)
finish_time = time()
print(f"Fibonacci from {n} is {result}")
print(finish_time - start_time)






