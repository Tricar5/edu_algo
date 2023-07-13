"""
URL: https://leetcode.com/problems/fruit-into-baskets/description/
"""

from collections import defaultdict
from typing import List

class Solution:
    def longestSub(self, s: str, k: int) -> int:

        longest = 0
        l = 0
        counts = defaultdict(int)

        for r in range(len(s)):
            counts[s[r]] += 1

            while len(counts) > k:

                counts[s[l]] -= 1

                if counts[s[l]] == 0:
                    del counts[s[l]]
                l += 1

            longest = max(longest, r - l + 1)

        return longest