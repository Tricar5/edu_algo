"""
URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""


class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter

        n, m = len(s), len(p)
        if n < m:
            return

        ans, cs, cp = [], Counter(s[0:m]), Counter(p)

        if cs == cp: ans.append(0)

        for i in range(n - m):
            prev, curr = s[i], s[i + m]

            cs[prev] -= 1

            if cs[prev] == 0:
                del cs[prev]

            cs[curr] += 1

            if cs == cp:
                ans.append(i + 1)

        return ans