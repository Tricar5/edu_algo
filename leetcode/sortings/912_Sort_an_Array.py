import random
from typing import List

"""
Algorithms:

- Quicksort ( n log n)
- Merge Sort (n log n)
- Heap Sort (n log n)
"""

arr = [random.randint(0, 10 * 6) for i in range(10 ** 3)]


# Quick Sort

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        pivot = nums[0]
        left = [x for x in nums[1:] if x < pivot]
        right = [x for x in nums[1:] if x >= pivot]
        return self.sortArray(left) + [pivot] + self.sortArray(right)


# Merge Sort
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            left = arr[L:M + 1]
            right = arr[M + 1:R + 1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1


        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l + r) // 2

            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)

# Heap Sort
