# 144 Traverse a Binary Tree
# Definition for a binary tree node.
import typing as tp
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: tp.Optional[TreeNode]) -> tp.List[int]:

        stack = []
        ans = []

        while root or stack:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right

        return ans


#  3
#   \
#    2
#   /
#  1
class Solution:

    def inorderTraversal(self, root):

        stack = []
        ans = []


        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            ans.append(root.val)
            root = root.right

        return ans


class Solution:
    def postorderTraversal(self, root: tp.Optional[TreeNode]) -> tp.List[int]:
        stack = []
        ans = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            temp = stack[-1].right

            if temp:
                root = temp
            else:
                temp = stack.pop()

                ans.append(temp.val)

                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    ans.append(temp.val)
        return ans


c = Solution()

root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))

print(c.postorderTraversal(root))
