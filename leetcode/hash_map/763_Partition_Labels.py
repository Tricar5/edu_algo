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


Основная идея:

1) Создать хэш-мапу с каждым последним индексом для символа пройдя по строке
2) Считать размер партиции во втором проходе
3) Счита

"""

from typing import List

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        last_idx = {}

        for i, c in enumerate(s):
            last_idx[c] = i

        ans = []
        size, end = 0, 0

        for i, c in enumerate(s):
            size += 1

            end = max(end, last_idx[c])
            if i == end:
                ans.append(size)
                size = 0

        return ans



c = Solution()


s = "ababcbacadefegdehijhklij"
print(c.partitionLabels(s))