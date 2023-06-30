"""



"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        MAP = {"(" : ")",
               "{": "}",
               "[": "]"}

        stack = []

        for p in s:

            if p in MAP.keys():
                stack.append(p)

            elif len(stack) == 0:
                return False

            elif MAP[stack.pop()] != p:
                return False

        if len(stack):
            return False

        return True
