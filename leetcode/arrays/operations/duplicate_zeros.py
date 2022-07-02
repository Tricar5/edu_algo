# Inserting elements

arr = [1,0,2,3,0,4,5,0]

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dup = 0
        len_ = len(arr) - 1

        for i in range(len_ + 1):
            if i > len_ - dup:
                break
            if arr[i] == 0:
                if i == len_ - dup:
                    arr[len_] = 0
                    len_ -= 1
                    break
                dup += 1

        last = len_ - dup

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + dup] = 0
                dup -= 1
                arr[i + dup] = 0
            else:
                arr[i + dup] = arr[i]


sol = Solution()

sol.duplicateZeros(arr)
