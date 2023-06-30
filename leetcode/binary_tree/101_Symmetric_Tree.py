"""
URL: https://leetcode.com/problems/symmetric-tree/description/
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = []

        def check_symmetric(arr: List[int | None]):
            m = len(arr) // 2

            r_arr = arr[::-1]

            return arr[:m] == r_arr[:m]

        if not root:
            return False

        queue.append(root)

        while queue:
            next_level = []
            vals = []

            for node in queue:

                if node.left:
                    next_level.append(node.left)
                    vals.append(node.left.val)
                else:
                    vals.append(None)

                if node.right:
                    next_level.append(node.right)
                    vals.append(node.right.val)
                else:
                    vals.append(None)

            if not check_symmetric(vals):
                return False

            queue = next_level

        return True

# DFS

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(l_node, r_node):
            if l_node == None or r_node == None:
                return l_node == r_node
            if l_node.val != r_node.val:
                return False
            return check(l_node.left, r_node.right) and check(l_node.right, r_node.left)

        return check(root.left, root.right)