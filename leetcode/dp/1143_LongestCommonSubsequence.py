import dataclasses
from typing import Tuple


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if text1[i] == text2[j]:
                    matrix[i][j] = matrix[i + 1][j + 1] + 1
                else:
                    matrix[i][j] = max(matrix[i + 1][j], matrix[i][j + 1])

        return matrix[0][0]


@dataclasses.dataclass
class TestCase:
    input_data: Tuple[str, str]
    expected: int


test_cases = [
    TestCase(
        input_data=('abcde', 'ace'),
        expected=3,
    ),
    TestCase(
        input_data=('abc', 'abc'),
        expected=3,
    ),
    TestCase(
        input_data=('abc', 'def'),
        expected=0,
    )
]

if __name__ == '__main__':
    c = Solution()
    for t in test_cases:
        result = c.longestCommonSubsequence(*t.input_data)
        print(f'Test case {t.input_data[0]}: {t.expected}')
        assert result == t.expected