"""
URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OP = {
            "+" : lambda x, y : x + y,
            "-" : lambda x, y : x - y,
            "/" : lambda x, y : x / y,
            "*" : lambda x, y : x * y,
        }
        stack = []

        for t in tokens:

            if t in OP:
                b = stack.pop()
                a = stack.pop()
                res = int(OP[t](a, b))
                stack.append(res)

            else:
                stack.append(int(t))

        return stack[0]