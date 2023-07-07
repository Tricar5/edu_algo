"""
URL: https://leetcode.com/problems/path-sum/description/

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        def dfs(node, cur):

            if not node:
                return False

            if node.val + cur == targetSum and not node.left and not node.right:
                return True

            return dfs(node.left, cur + node.val) or dfs(node.right, cur + node.val)

        return dfs(root, 0)


# Stack from Neetcode


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        de = [
            (root, sum - root.val),
        ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
