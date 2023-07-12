"""
URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target:
                return [l + 1, r + 1]
            elif two_sum < target:
                l += 1
            else:
                r -= 1

        return