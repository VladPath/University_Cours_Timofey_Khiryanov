def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else n

print(fib(10))