"""
URL: https://leetcode.com/problems/koko-eating-bananas/description/

Идеи:
    1. Бинарный поиск по скорости
    2. Оптимизируем функцию по времени "поедания"
"""

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = max(piles)

        def helper(sp, arr):

            time = 0

            for pile in arr:
                # округление вверх
                time += math.ceil(pile / sp)

            return time

        while l <= r:

            mid = (l + r) // 2

            ttl_time = helper(mid, piles)

            if ttl_time <= h:

                res = min(res, mid)
                # уменьшаем скорость
                r = mid - 1

            else:
                # увеличиваем скорость
                l = mid + 1

        return res