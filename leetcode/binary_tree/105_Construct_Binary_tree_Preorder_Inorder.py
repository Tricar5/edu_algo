# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def array_to_tree(left, right):
            nonlocal preorder_index

            # Случай, когда нет элементов для построения дерева
            if left > right:
                return None

            # Выбираем элемент по preorder_index в качестве корня и увеличиваем его
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            # Строим левое и правое поддеревья
            # исключаем inorder_index_map[root_value] поскольку это корень

            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        # инициализация индекса для шага
        preorder_index = 0
        # инициализация hash таблицы для хранения значения и индекса
        # в структуре по порядке узлов
        inorder_index_map = {}

        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)
