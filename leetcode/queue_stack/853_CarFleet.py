"""

URL:

"""


class Solution:

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # [(10, 8]
        cars = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for pos, sp in sorted(cars)[::-1]:
            stack.append((target - pos) / sp)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)