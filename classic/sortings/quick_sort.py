class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[0]
            left = [x for x in nums[1:] if x < pivot]
            right = [x for x in nums[1:] if x >= pivot]
        return self.sortArray(left) + [pivot] + self.sortArray(right)
