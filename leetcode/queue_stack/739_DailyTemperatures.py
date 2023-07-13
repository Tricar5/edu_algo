"""
URL: https://leetcode.com/problems/daily-temperatures/description/
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, j = stack.pop()
                ans[j] = i - j

            stack.append((temp, i))

        return ans