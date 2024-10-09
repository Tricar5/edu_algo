from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return None

        l, r = 0, len(height)-1

        left_max, right_max = height[l], height[r]
        res = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res


c = Solution()

tests = [
    [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
    [[4, 2, 0, 3, 2, 5], 9],
]
if __name__ == '__main__':
    for test in tests:
        print(test)
        assert c.trap(test[0]) == test[1]
