class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        nums1[:n] = nums2[:n]


nums1 = [4,0,0,0,0]
m = 1
nums2 = [1,2,5,6]
n = 4

sol = Solution()

sol.merge(nums1,m,nums2,n)
print(nums1)