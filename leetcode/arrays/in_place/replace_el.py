# Replace elements to their right greatest


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        r_greatest = arr[-1]

        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):

            if arr[i] > r_greatest:
                t = arr[i]

                arr[i] = r_greatest
                r_greatest = t

            else:
                arr[i] = r_greatest

        return arr

arr = [17,18,5,4,6,1]

sol = Solution()

print(arr)
sol.replaceElements(arr)