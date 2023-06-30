"""
URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        cur_min = float("inf")

        while l < r:

            mid = (l + r) // 2

            cur_min = min(cur_min, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid - 1

        return min(cur_min, nums[l])