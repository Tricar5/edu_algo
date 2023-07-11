"""
URL: https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        l = 0
        maxf = 0

        # Двигаем окно
        for r in range(len(s)):
            # Обновление таблицы встречаемости
            count[s[r]] = 1 + count.get(s[r], 0)

            # Счетчик для максимального числа встречаемого символа в окне
            maxf = max(maxf, count[s[r]])

            # Проверяем можем ли мы за предоставленное количество попыток
            # изменить все символы в окне
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
