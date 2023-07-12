"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if not len(nums):
            return 0

        ans = [0 for i in range(len(nums))]
        l_prefix = [0 for i in range(len(nums))]
        r_prefix = [0 for i in range(len(nums))]

        l_prefix[0], r_prefix[len(nums) - 1] = 1, 1

        # Making left prefix
        for i in range(1, len(nums)):
            l_prefix[i] = l_prefix[i - 1] * nums[i - 1]

        # Making right prefix (suffix)
        for j in range(len(nums) - 2, -1, -1):
            r_prefix[j] = r_prefix[j + 1] * nums[j + 1]

        for i in range(len(nums)):
            ans[i] = l_prefix[i] * r_prefix[i]

        return ans


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



c = Solution()

arr = [1,2,3,4]

print(c.productExceptSelf(arr))