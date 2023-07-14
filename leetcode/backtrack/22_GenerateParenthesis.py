"""
URL: https://leetcode.com/problems/generate-parentheses/description/
"""


class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(opened, closed, current):

            if opened == closed == n:
                result.append(current)
                return

            if opened < n:
                backtrack(opened + 1, closed, current + "(")

            if closed < opened:
                backtrack(opened, closed + 1, current + ")")

        backtrack(0, 0, "")

        return result
