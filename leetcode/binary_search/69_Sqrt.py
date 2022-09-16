class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 1
        r = x

        while l < r:
            mid = (l + r) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                r = mid
            else:
                l = mid + 1

        return l if l == 1 else l - 1

c = Solution()

tests = [(4, 2),
         (16, 4),
         (1, 1),
         (8, 2),
         (5, 2)]

for i, test in enumerate(tests):
    x, ans = test
    assert c.mySqrt(x) == ans, AssertionError(f'Test {i} failed.\nReturned: {c.mySqrt(x)}\nExpected {ans}')