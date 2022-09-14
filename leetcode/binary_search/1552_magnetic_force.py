class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position = sorted(position)

        # helper function
        def cnt_mid(distance):
            # put the first one at 1
            count = m - 1
            lastplace = position[0]
            for i in range(1, len(position)):
                if count == 0:
                    return True
                # record the last place to put a ball
                if position[i] - lastplace >= distance:
                    count -= 1
                    lastplace = position[i]
                else:
                    continue
            #  when reach the end of the list, we need this to check if count meets requirement
            if count == 0:
                return True
            return False

        # initialize the min and max distance
        left = 1
        right = (position[-1] - position[0]) // (m - 1) + 1

        while left < right:
            mid = left + (right - left) // 2
            # shrink left
            if cnt_mid(mid):
                left = mid + 1
            else:
                # shrink right
                right = mid

            # when terminates, left is added 1, so we need to subtract 1 from left
        return left - 1

c = Solution()

n, m = list(map(int, input().split()))
positions = list(map(int, input().split()))

print(c.maxDistance(positions, m))