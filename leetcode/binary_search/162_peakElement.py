class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return 0

        def check(m, arr):
            return arr[m-1] <= arr[m] >= arr[m+1]

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l+r) // 2

            if check(m, nums):
                return m
            elif nums[m-1] < nums[m]:
                l = m+1
            else:
                r = m

        return l


tests = [([1,2,1], {1}),
         ([1,2,3,1], {2}),
         ([1,2,1,3,5,6,4], {1,5}),
         ([1], {0}),
         ([1,2], {1})]

c = Solution()

for i, test in enumerate(tests):
    assert c.findPeakElement(test[0]) in test[1], AssertionError(f'Test {i} failed\nGet: {c.findPeakElement(test[0])}')