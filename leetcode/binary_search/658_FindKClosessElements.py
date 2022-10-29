from typing import List

"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        def collect_ans(pos, k, x):

            ans = []

            if abs(x - arr[pos-1]) <= abs(x - arr[pos-1]):
                l, r = pos-1, pos
            else:
                l, r = pos, pos + 1

            while k > 0:

                if l >= 0 and r < len(arr):
                    if abs(x - arr[l]) <= abs(x - arr[r]):
                        ans = [arr[l]] + ans
                        l -= 1

                    else:
                        ans = ans + [arr[r]]
                        r += 1

                elif l >= 0:
                    ans = [arr[l]] + ans
                    l -= 1

                elif r < len(arr):
                    ans = ans + [arr[r]]
                    r += 1

                k -= 1

            return ans

        if len(arr) == 1:
            return arr

        left, right = 0, len(arr) - 1

        if len(arr) == 2:
            return collect_ans(0, k, x)

        while left + 1 < right:
            mid = (left + right) // 2

            if arr[mid] == x:
                break
            elif arr[mid] >= x:
                right = mid
            else:
                left = mid

        if k > 1:
            while arr[mid] == arr[mid - 1]:
                mid -= 1

        return collect_ans(mid, k, x)

"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # since this is a sorted array
        # we can just find a range i to i+k-1
        # And if its mid range is closest to k
        # then this range is right
        l, r = 0, len(arr) - k
        while l < r:

            mid = l + (r - l) // 2  # check left point
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l:l + k]


c = Solution()

arr = list(map(int, input().split()))
k = int(input())
x = int(input())


print(c.findClosestElements(arr, k, x))

# arr = [1,2,3,4,5], k = 4, x = 3
# arr = [1,2], k = 2 x = 2
# arr = [1,2,3,4,5], k = 4, x = 3
# arr = [1,2,3,4,5], k = 4, x = 3
# arr = [1,2,3,4,5], k = 4, x = -1
# [1,2,3,4,4,4,4,5,5] 3, 3