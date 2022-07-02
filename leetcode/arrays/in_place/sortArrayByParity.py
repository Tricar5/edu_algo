#  Sort Array By Parity

#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#Return any array that satisfies this condition.

# А если идти с двух сторон???


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        i = 0

        for j in range(1, len(nums)):

            if nums[j] % 2 == 0 and nums[i] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

            if nums[i] % 2 == 0:
                i += 1

        return nums

sol = Solution()

nums = [2,4,1,0]

sol.sortArrayByParity(nums)