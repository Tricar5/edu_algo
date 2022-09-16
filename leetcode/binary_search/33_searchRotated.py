class Solution:

    def search(self, nums: list[int], target: int) -> int:
        """
        Идея: давайте оценивать с каким массивом мы имеем дело
        Если до мид индекс возрастает от левого
            Если таргет заключен между левой и мид значениями, то обычный бинпоиск получается в этой части
            Иначе: двигаем l на место mid
        Иначе (Левый больше мидового):
            Если таргет меньше правого и больше мида - идем вправо
            Иначе: идем влево
        """
        l = 0
        r = len(nums) - 1


        while l <= r:
            m = (l+r) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target <= nums[r] and target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

c = Solution()


# 7, 8, 9, 1, 2, 3, 4, 5, 6

#

#  5, 6, 7, 8, 9, 1, 2, 3, 4

tests = [([4,5,6,7,0,1,2], 0, 4),
         ([1,3], 3, 1),
        ([5,1,3], 5, 0),
         ([0, 2, 3, 4, 5,], 1, -1),
         ([1], 0, -1),
         ([1], 1, 0),
         ([1, 3], 1, 0),
         ]

for i,test in enumerate(tests):
    nums, target, exp = test
    ans = c.search(nums,target)
    assert ans == exp, AssertionError(f'Test {i} failed.\nReturned: {ans}\nExpected {exp}')