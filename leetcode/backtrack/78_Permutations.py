"""
URL: https://leetcode.com/problems/permutations/description/
"""


class Solution:

    def permute(self, nums: list[int]) -> list[list[int]]:

        result = []

        def backtrack(current, nums):

            if current == len(nums):
                result.append(nums[:])
                return

            for i in range(current, len(nums)):

                nums[i], nums[current] = nums[current], nums[i]
                backtrack(current + 1, nums)
                nums[i], nums[current] = nums[current], nums[i]

        backtrack(0, nums)

        return result


c = Solution()

nums = [1, 2, 3]

print(len(c.permute(nums)))