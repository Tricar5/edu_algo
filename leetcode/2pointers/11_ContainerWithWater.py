"""

"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        i, j = 0, len(height) - 1

        while i < j:

            cur_area = min(height[j], height[i]) * (j - i)

            max_area = max(max_area, cur_area)

            if height[i] > height[j]:
                j -= 1

            elif height[i] < height[j]:
                i += 1

            else:
                i += 1
                j -= 1

        return max_area