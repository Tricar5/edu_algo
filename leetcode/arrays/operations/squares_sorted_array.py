#   Squares of a Sorted Array


input_var = [-4,-1,0,3,10]

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return self.sortElements(self.squareElements(nums))

    def squareElements(self, nums: list[int]) -> list[int]:
        return [x*x for x in nums]

    def sortElements(self, nums: list[int]) -> list[int]:

        if len(nums) < 2:
            return nums

        else:
            p_idx = len(nums)//2
            pivot = nums.pop(p_idx)

            less = [x for x in nums if x <= pivot]

            greater = [x for x in nums if x > pivot]

            return self.sortElements(less) + [pivot] + self.sortElements(greater)


solver = Solution()

solver.sortedSquares(input_var)