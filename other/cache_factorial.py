
from functools import cache
import time


#@cache

fibonacci_cache = {}

def fibonacci(n):

    if n in fibonacci_cache.keys():
        return fibonacci_cache[n]
    elif n in {0,1}:
        return n
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
        fibonacci_cache[n] = value
        return value


def fibonacci_loop(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        for i in range(1, n-1):
            sequence.append(sequence[i-1] + sequence[i])
    return sum(sequence)

ts = time.time()
f_1 = fibonacci(900)
te = time.time()
print(f'{te-ts:4f} sec')

ts_1 = time.time()
f_2 = fibonacci_loop(899)
te_1 = time.time()
print(f'{te_1-ts_1:4f} sec')

print(f_1)
print(f_2)