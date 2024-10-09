import dataclasses
from typing import List

from leetcode.binary_search.learn.binary_search import target


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(index, comb, total):
            if total == target:
                ans.append(comb[:])
                return

            for i in range(index, len(candidates)):
                new_total = total + candidates[i]

                if new_total > target:
                    return

                comb.append(candidates[i])
                backtrack(i, comb, new_total)
                comb.pop()

        backtrack(0, [], 0)

        return ans


@dataclasses.dataclass
class TestData:
    input_arr: List[int]
    target: int
    output_arr: List[List[int]]


tests = [
    TestData(input_arr=[2, 3, 6, 7], target=7, output_arr=[[2, 2, 3], [7]]),
    TestData(input_arr=[2, 3, 5], target=8, output_arr=[[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    TestData(input_arr=[2], target=1, output_arr=[]),
]

if __name__ == '__main__':
    c = Solution()
    for t in tests:
        res = c.combinationSum(t.input_arr, t.target)
        assert res == t.output_arr