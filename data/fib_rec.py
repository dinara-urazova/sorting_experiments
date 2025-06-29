from sys import argv
from time import time



def fib(num):
    global cache
    if cache[num] != 'None':
        
    if num <= 1:
        return num
    return (fib(num-1) + fib(num-2))
 


n = int(argv[1])
cache = [None] * n

start_time = time()
res = fib(n)

print(f"Fibonacci from {n} is {res}")
print(cache)
finish_time = time()
print(finish_time - start_time)





