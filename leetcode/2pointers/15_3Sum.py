"""
URL:
"""

# Не оптимальное решение - brute force

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Ответ
        ans = []
        # для чекинга вхождений
        checker = set()

        for x in range(len(nums) - 2):
            for y in range(x + 1, len(nums) - 1):
                for z in range(y + 1, len(nums)):
                    # Проверяем положительное условие
                    if nums[x] + nums[y] + nums[z] == 0:
                        # Делаем проверочный массив для добавления и проверки в checker
                        t = sorted([nums[x], nums[y], nums[z]])
                        if tuple(t) not in checker:
                            checker.add(tuple(t))
                            ans.append(t)
        return ans


# Более оптимальное решение с сортировкой

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        check_set = set()

        nums.sort()

        x = 0

        while x < len(nums) - 2:

            l, r = x + 1, len(nums) - 1

            while l < r:

                check_sum = nums[x] + nums[l] + nums[r]

                if check_sum == 0 and (nums[x], nums[l], nums[r]) not in check_set:
                    ans.append([nums[x], nums[l], nums[r]])
                    check_set.add((nums[x], nums[l], nums[r]))
                elif check_sum > 0:
                    r -= 1
                else:
                    l += 1

            x += 1

        return ans


# Оптимизированное без хэшмапы

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()

        for i, a in enumerate(nums):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1]:
                        l += 1

        return ans