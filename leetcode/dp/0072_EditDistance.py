"""

|   | h | o | r | s | e |
|   |   |   |   |   |   |
| r |   |   |   |   |   |
| o |   |   |   |   |   |
| s |   |   |   |   |   |


"""


class Solution:

    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word1), len(word2)
    #
    #     # Create a table to store results of subproblems
    #     dp = [[0] * (n + 1) for _ in range(m + 1)]
    #
    #     for i in range(m + 1):
    #         dp[i][0] = i
    #     for j in range(n + 1):
    #         dp[0][j] = j
    #
    #     # Fill the rest of dp[][]
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if word1[i - 1] == word2[j - 1]:
    #                 dp[i][j] = dp[i - 1][j - 1]
    #             else:
    #                 change = dp[i][j - 1]
    #                 add = dp[i - 1][j]
    #                 delete = dp[i - 1][j - 1]
    #                 dp[i][j] = 1 + min(add, change, delete)
    #
    #     return dp[m][n]

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        if n > m:
            # убедимся что n <= m, чтобы использовать минимум памяти O(min(n, m))
            word2, word1 = word1, word2
            n, m = m, n

        current_row = range(n + 1)

        for i in range(1, m + 1):

            previous_row, current_row = current_row, [i] + [0] * n

            for j in range(1, n + 1):

                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, current_row[j - 1]

                if word1[j - 1] != word2[i - 1]:
                    change += 1

                current_row[j] = min(add, delete, change)

        return current_row[n]


tests = [
    [['ros', 'horse'], 3],
    [['intention', 'execution'], 5],
]

if __name__ == '__main__':
    c = Solution()
    for test in tests:
        assert c.minDistance(*test[0]) == test[1]
