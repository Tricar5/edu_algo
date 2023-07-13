"""
URL: https://leetcode.com/problems/fruit-into-baskets/description/
"""

from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        k = 2
        longest = 0
        l = 0
        counts = defaultdict(int)

        for r in range(len(fruits)):
            counts[fruits[r]] += 1

            while len(counts) > k:

                counts[fruits[l]] -= 1

                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
                l += 1

            longest = max(longest, r - l + 1)

        return longest