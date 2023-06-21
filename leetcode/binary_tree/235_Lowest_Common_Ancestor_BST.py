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

        elif root.val == p.val or root.val == q.val:
            return root

        elif min(p.val, q.val) < root.val < max(p.val, q.val):
            return root

        #l = self.lowestCommonAncestor(root.left, p, q)
        #r = self.lowestCommonAncestor(root.right, p, q)

        return lowestCommonAncestor(root.left, p, q) or lowestCommonAncestor(root.right, p, q)