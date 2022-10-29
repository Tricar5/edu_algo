"""def binarySearch(nums, target):
    pair = [-1, -1]

    if len(nums) == 0:
        return pair


    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1"""

from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def expand(l, r, target):

            while l > 0 and nums[l - 1] == target:
                l -= 1

            while r < len(nums) - 1 and nums[r + 1] == target:
                r += 1

            return [l, r]

        pair = [-1, -1]

        if not nums:
            return pair

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return expand(mid, mid, target)

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return pair