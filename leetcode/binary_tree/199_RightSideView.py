"""

URL: https://leetcode.com/problems/binary-tree-right-side-view/description/

Идея: 1) Level Order Traversal (BFS - queue)
2) Потом из каждого уровня извлекаем последний элемент

"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return None

        # Level Order Traversal
        levels = []
        q = [root]

        while q:

            level = []
            nxt = []

            for n in q:
                level.append(n.val)
                if n.left:
                    nxt.append(n.left)
                if n.right:
                    nxt.append(n.right)

            levels.append(level)
            q = nxt

        # Result Query Set
        ans = []

        for lvl in levels:
            ans.append(lvl[-1])

        return ans


"""
Более оптимальный код по памяти 
"""
import collections

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
