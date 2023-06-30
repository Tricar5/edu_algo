"""
Идея: Битовый сдвиг

Использовать исключающее ИЛИ

Что будет происходить?

[4, 1, 2, 1, 2]

4 - 1 0 0
1 - 0 0 1
2 - 0 1 0
1 - 0 0 1
2 - 0 1 0

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]

        for num in nums[1:]:

            ans = ans ^ num

        return ans
