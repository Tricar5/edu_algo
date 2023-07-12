"""

"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n_set = set(nums)

        for num in nums:

            if num - 1 not in n_set:
                curr_res = 1

                while num + curr_res in n_set:
                    curr_res += 1

                ans = max(ans, curr_res)
        return ans