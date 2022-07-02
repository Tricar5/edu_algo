#https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3255/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if (len(nums) == 0 or nums == None): return 0

        i = 0


        for j in range(1, len(nums)):

            if nums[j] != nums[i] :
                i += 1
                nums[i] = nums[j]
        return i+1


arr = [0,0,1,1,1,2,2,3,3,4]

sol = Solution()

print(sol.removeDuplicates(arr))

print(len(set(arr)))