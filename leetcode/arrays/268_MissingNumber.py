"""

URL: https://leetcode.com/problems/missing-number/description/
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        max_range = len(nums)
        return sum(range(0, max_range + 1)) - sum(nums)