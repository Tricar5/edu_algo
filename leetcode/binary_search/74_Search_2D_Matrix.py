"""
URL: https://leetcode.com/problems/search-a-2d-matrix/description/

Идеи: 1) Проверяем по последнему элементу в ряду
2) Делаем Binary Search
"""


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                break

        row = matrix[i]

        l, r = 0, len(matrix[0])

        while l < r:

            mid = (r + l) // 2

            if row[mid] == target:
                return True

            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid

        return False