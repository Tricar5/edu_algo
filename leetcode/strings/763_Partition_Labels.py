"""
763. Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.


Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

"""

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        ans = []

        lastIndex = dict()

        # Making hash table
        for i, c in enumerate(s):
            lastIndex[c] = i

        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1

            end = max(lastIndex[c], end)

            if i == end:
                ans.append(size)
                size = 0

        return ans



c = Solution()


s = "ababcbacadefegdehijhklij"
print(c.partitionLabels(s))