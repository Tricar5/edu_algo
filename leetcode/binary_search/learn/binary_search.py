"""
Binary Search is generally composed of 3 main sections:

Pre-processing - Sort if collection is unsorted.

Binary Search - Using a loop or recursion to divide search space in half after each comparison.

Post-processing - Determine viable candidates in the remaining space.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1

c = Solution()

tests = [([-1,0,3,5,9,12], 9, 4),
         ([0, 2, 3, 4, 5,], 1, -1),
         ([5], 5, 0)]

for i,test in enumerate(tests):
    nums, target, ans = test
    assert c.search(nums,target) == ans, AssertionError(f'Test {i} failed')