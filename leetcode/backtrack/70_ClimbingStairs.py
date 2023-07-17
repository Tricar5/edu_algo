"""

"""


class Solution:

    def climbStairs(self, n: int) -> int:
        memo = {}

        def backtrack(goal):

            if goal == 0 or goal == 1:
                return 1

            if goal not in memo:
                memo[goal] = backtrack(goal - 1) + backtrack(goal - 2)

            return memo[goal]

        return backtrack(n)