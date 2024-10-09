from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        possiblesums = set()
        target = total / 2

        for i in range(len(nums)):
            if nums[i] == target:
                return True
            # Store all the unique possible sums that are now possible with our nums[i]
            newsums = {nums[i]}
            for s in possiblesums:
                if s+nums[i] == target:
                    return True
                if s+nums[i] < target:
                    newsums.add(s+nums[i])
            possiblesums = possiblesums.union(newsums)

        return False

tests = [
    [[1, 5, 11, 5], True],
    [[1, 2, 3, 5], False],
    [[2, 2, 1, 1], True],
    [[0, 0, 0, 0], True],
    [[1, 0, 1, 2], True],
    [[0, 0], True],
    [[0], True]
]

if __name__ == "__main__":
    c = Solution()

    for t in tests:
        assert c.canPartition(t[0]) == t[1]
