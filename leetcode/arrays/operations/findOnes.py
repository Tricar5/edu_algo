# У нас есть массив, у каждого элемента массива есть пара кроме одного
# Нужно найти этот элемент

import pytest


# O(n logn)

def ArrFindOne(arr):
    arr_s = sorted(arr)

    for i in range(0, len(arr_s)):
        if (i == 0 or arr_s[i] != arr_s[i - 1]) and (i == len(arr_s) - 1 or arr_s[i] != arr_s[i + 1]):
            return arr_s[i]


# O(n) + Space complexity

def ArrFindOne(arr):
    s_el = set()

    for i in range(len(arr)):

        if arr[i] in s_el:
            s_el.remove(arr[i])

        else:
            s_el.add(arr[i])

    return s_el.pop()


# O(n) - fucking XOR

from functools import reduce # reduce применяется итерируемо применяется ко всем элементам

def ArrFindOne(arr):
    return reduce(lambda x, y: x ^ y, arr)


tests = (
    ([1, 2, 3, 2, 1], 3),
    ([1], 1),
    ([2, 3, 2, 3, 5], 5),
    ([2, 2, 1], 1),
    ([1, 2, 2, 3, 3], 1)
)

for test in tests:
    assert test[1] == ArrFindOne(test[0]), AssertionError(test[0], ArrFindOne(test[0]))
