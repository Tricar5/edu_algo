"""
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    # Time complexity: O(N)
    # Space complexity: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None

        # Общий предок - это или P или Q
        elif root.val == p.val or root.val == q.val:
            return root

        # Проверка позиции текущей ноды. Если она между левым и правым - мы нашли общего предка
        elif min(p.val, q.val) < root.val < max(p.val, q.val):
            return root

        # Одно из условий должно выполняться
        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)