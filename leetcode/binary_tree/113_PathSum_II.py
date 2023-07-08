"""
URL: https://leetcode.com/problems/path-sum-ii/description/

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []

        def dfs(root, nodes):
            if not root:
                return

            nodes = nodes + [root.val]

            if not root.left and not root.right:
                if sum(nodes) == targetSum:
                    ans.append(nodes)

            if root.left:
                dfs(root.left, nodes)

            if root.right:
                dfs(root.right, nodes)

        dfs(root, [])
