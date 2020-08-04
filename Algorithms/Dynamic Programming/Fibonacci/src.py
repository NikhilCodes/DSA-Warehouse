"""
The sequence is:

1 1 2 3 5 8 13 21 34 55 89 144 ...
"""
import functools
import timeit


# Plain Fibonacci Solver
def fibonacci_vanilla(n):  # O(2^n)
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_vanilla(n - 1) + fibonacci_vanilla(n - 2)

## ----------------------------------------------------------------- ##

# Optimized Fibonacci Solver

# caching Function Decorator
def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


# One can use @memoize or @functools.lru_cache(128) to get performance benefits over Vanilla fibonacci
@memoize            # O(n)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print('Vanilla Fibonacci:', timeit.timeit('fibonacci_vanilla(30)', globals=globals(), number=1), 'seconds')
    print('Memoized Fibonacci:', timeit.timeit('fibonacci(30)', globals=globals(), number=1), 'seconds')
