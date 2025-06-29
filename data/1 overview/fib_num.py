from sys import argv
from time import time

n = int(argv[1])
print(n)

def fib(n):
    start_time = time()
    counter = 0
    first = 0
    second = 1

    while counter <= n:
        print(first)
        first, second = second, first + second
        counter += 1
        finish_time = time()
    print(finish_time - start_time)

fib(n)
 
 
