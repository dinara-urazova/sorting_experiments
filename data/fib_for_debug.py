def fibonacci (n: int) -> int:
    if n <= 1:
        return n
    fib_n_1 = fibonacci(n-1)
    fib_n_2 = fibonacci(n-2)
    fib_n = fib_n_1 + fib_n_2
    return fib_n


n = int(input())
fib_n = fibonacci(n)
print(fib_n)
