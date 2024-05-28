"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Подходы:

1. Сортировка. T(C) = nlog(n)
2. Max HeapQ.
3. Quick Select

"""
import heapq
from typing import List

# Sorted
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

# HeapQ

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap= []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

        return heap[0]


# Quick Select
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quick_select(1, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)
