#Given an integer n, return the least number of perfect square numbers that sum to n.

#A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

#Example 1:

#Input: n = 12
#Output: 3
#Explanation: 12 = 4 + 4 + 4.

"""

Решаем рекурсивно

"""
import collections


class Solution(object):
    def __init__(self):
        self._d = dict()

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in self._d.keys():
            return self._d[n]

        sq = int(n ** 0.5)

        if sq * sq == n:
            self._d[n] = 1
            return 1

        res = n

        for i in range(1, sq+1):
            res = min(res, self.numSquares(n - i * i))

        self._d[n] = res + 1

        return self._d[n]


# BFS

class Solution(object):

    def numSquares(self, n):
        """
        Use list comprehension to generate all perfect squares that are less than the target n.
        Use queue to store [n, d] (node and current depth).
        Use a set seen to record the node we have seen to avoid duplicated calculation.
        BFS the queue, when the node is a perfect square, return the current depth d;
        Otherwise, if we haven't calculate node-s, add node-s to the seen and the (node-s, d+1) to the queue.
        :param n:
        :return:
        """
        if (n <= 0):
            return 0

        sq = [x*x for x in range(1, n) if x*x <= n]

        queue = collections.deque()

        seen = set()

        queue.append([n, 1])

        while queue:
            node, d = queue.popleft()

            if node in sq:
                return d

            for s in sq:
                if node <= s:
                    break

                if node-s not in seen:
                    seen.add(node-s)
                    queue.append([node-s, d+1])

        return n


# Lagrange Four Square Theorem
#
#


c = Solution()

print(c.numSquares(16))
