
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


c = Solution()

arr = [1,2,3,4]

print(c.productExceptSelf(arr))