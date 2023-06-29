"""
1381. Design a Stack With Increment Operation

Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.

URL: https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.m = maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top < self.m - 1:
            self.arr.append(x)
            self.top += 1

    def pop(self) -> int:
        if self.top == -1:
            return -1
        self.top -= 1
        return self.arr.pop(-1)

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.top + 1)):
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)