"""
URL: https://leetcode.com/problems/find-the-duplicate-number/description/

Идея:
1) Массив как линкед лист. Так как диапазон с одним дубликатом, то создается цикл
2) Используем технику Floyd's - быстрый и медленный указатель (x, 2x)

3) От начала пройдем, пока slow и slow2 не встретятся - определим начало цикла

[0, 1, 2, 3, 4,]
[1, 3, 4, 2, 2]

nums[0] -> 1
nums[1] -> 3
nums[3] -> 2 / начало цикла
nums[2] -> 4 # цикл
nums[4] -> 2 # цикл
nums[2] -> 4

"""


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow