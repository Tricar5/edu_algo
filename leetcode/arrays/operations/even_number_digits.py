#Find numbers with even number of digits
input_var = [12,345,2,6,7896]

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for el in nums:
            if self.countDigits(el) % 2 == 0:
                count += 1

        return count

    def countDigits(self, num: int) -> int:

        length = 0

        while num != 0:

            num = num // 10
            length += 1
        return length

solver = Solution()

solver.findNumbers(input_var)