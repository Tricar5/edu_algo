"""
URL : https://leetcode.com/problems/deepest-leaves-sum/description/

Идея:
1) Пройти каждый уровень дерева с помощью breadth-first search. Добавляя в очередь на каждом этапе ноду и её глубину
2) Для каждого уровня вычислить сумму
3) Взять максимальный уровень и вернуть его сумму

"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *
from collections import *

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        queue = [(root, 0)]
        deepest = defaultdict(int)

        while queue:
            node, deep = queue.pop(0)
            deepest[deep] += node.val

            if node.left:
                queue.append((node.left, deep + 1))

            if node.right:
                queue.append((node.right, deep + 1))

        return deepest[max(deepest)]