# Definition for a binary tree node.


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_traversal = []
        q_traversal = []

        def traverse(arr, node):

            if node:
                arr.append(node.val)

                traverse(arr, node.left)
                traverse(arr, node.right)
            else:
                arr.append(None)

        traverse(p_traversal, p)
        traverse(q_traversal, q)

        return p_traversal == q_traversal

    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        return (p.val== q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
