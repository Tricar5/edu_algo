# Zeros

class Solution:
    def moveZeroes_extra(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        num_sup = [el for el in nums if el != 0]

        len_sup = len(num_sup)

        for i in range(len(nums)):

            if i < len_sup:
                nums[i] = num_sup[i]

            else:
                nums[i] = 0

        return nums

    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        length = len(nums)

        for j in range(0,len(nums)):

            if nums[j] != 0:
                nums[i] = nums[j]
                i +=1

        for j in range(i, len(nums)):
            nums[j] = 0


        return nums

sol = Solution()

arr = [0,1,0,2,3,4,0,5,0]

sol.moveZeroes(arr)