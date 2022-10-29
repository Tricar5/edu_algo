class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        people_pos = (i for i, seat in enumerate(seats) if seat)

        prev, future = None, next(people_pos)

        ans = 0

        for i, seat in enumerate(seats):
            if seat:
                prev = i

            else:
                # Действует для переключения по итератору для закрытых интервалов
                while future is not None and future < i:
                    future = next(people_pos, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i

                ans = max(ans, min(left, right))

        return ans

# [0,0,0,0,0,1]
# [1,0,0,0,0,0]
# [1,0,0,0,1,1]