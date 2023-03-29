"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l, r = 0, len(nums) - 1

        while l <= r:
            # shifting to remove duplicate elements
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1

            m = (l + r) // 2

            if nums[m] == target:
                return True

            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target <= nums[r] and target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return False



c = Solution()

tests = [([4,5,6,7,0,1,2], 0, True),
         ([1,3], 3, True),
        ([5,1,3], 5, True),
         ([0, 2, 3, 4, 5,], 1, False),
         ([1], 0, False),
         ([1], 1, True),
         ([1, 3], 1, True),
         ]

for i,test in enumerate(tests):
    nums, target, exp = test
    ans = c.search(nums,target)
    assert ans == exp, AssertionError(f'Test {i} failed.\nReturned: {ans}\nExpected {exp}')
    print(f'Success {i}')