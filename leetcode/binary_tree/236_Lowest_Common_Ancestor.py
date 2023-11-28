"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Идея:

1) Depth-First Search

2) Рекурсия:
    - Проверка root - если он пустой, то мы добрались до нижней точки
    - Если root равен p / q, то он является предком

Формулировка алгоритма:
Если наш корень равен p или q - то мы нашли

Если из обоих поддеревьев мы нашли наш p и q, то наш корень - LCA

Если вернулось значение только из одного, то он и есть наш LCAё

Делаем это рекурсивно



"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution:

    # Time complexity: O(N)
    # Space complexity: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None

        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root

        else:
            return l or r