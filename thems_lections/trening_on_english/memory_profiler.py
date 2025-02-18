from memory_profiler import profile

@profile
def my_func():
    return [i for i in range(100)]

@profile
def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else n

print(fib(30))

print(my_func())
