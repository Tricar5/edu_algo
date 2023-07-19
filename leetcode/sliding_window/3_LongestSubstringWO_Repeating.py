"""
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Идея: 1) Скользящее окно по строке (l=0, r=0)
2) множество для хранения символов
3) Если символ встречается - удаляем символы по l, пока s[r] будет не внутри хэшмапы

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        chars = set()
        l = 0

        for r in range(len(s)):

            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            res = max(res, r - l + 1)

        return res