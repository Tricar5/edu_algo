"""
Дан массив arr[int], где необходимо осуществить проверку, что он монотонно возрастает до некоторого элемента, а потом монотонно убывает до конца
"""

class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # Идем вверх по элементам массива
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        if i == 0 or i == N-1:
            return False

        # Спускаемся
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1




#arr = [0,2,3,4,5,4,2,1]

arr = [2,1]

sol = Solution()

sol.validMountainArray(arr)