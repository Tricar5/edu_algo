# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:



        def traverse_node(node, cur_sum: int):

            cur_sum += node.val

            if not node.left and not node.right:
                return cur_sum == targetSum

            if cur_sum > targetSum:
                return False

            left = traverse_node(node.left, cur_sum)
            right = traverse_node(node.left, cur_sum)

            return max(left, right)

        if root:
            cur_sum = 0
            res = traverse_node(root, cur_sum)
            return res

        return False


nodes = [5,4,8,11,None,13,4,7,2,None,None,None,1]


n9 = TreeNode(1)
n8 = TreeNode(2)
n7 = TreeNode(7)
n6 = TreeNode(4, n9)
n5 = TreeNode(13)
n4 = TreeNode(11, n7, n8)
n3 = TreeNode(8, n5, n6)
n2 = TreeNode(4, n4)
n1 = TreeNode(5, n2, n3)

c = Solution()

print(c.hasPathSum(n1, 22))