"""
URL: https://leetcode.com/problems/contains-duplicate-ii/description/

"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}

        for i, num in enumerate(nums):
            if num in hash_map and i - hash_map[num] <= k:
                return True

            hash_map[num] = i

        return False