
class Solution:

    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        length = 0

        result = 0

        for i in range(len(nums)):

            if nums[i] == 0:

                length = 0

            if nums[i] == 1:

                length +=1

                result = max(result, length)

        return result

solver = Solution()

input_var = [1,1,0,0,1,1]

solver.findMaxConsecutiveOnes(input_var)