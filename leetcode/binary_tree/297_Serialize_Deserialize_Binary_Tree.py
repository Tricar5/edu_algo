"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # Структура для сохранения данных
        res = []

        def dfs(node):
            # Проверка на существование ноды
            if not node:
                # Поддерево закончилось - ставим заглушку
                res.append("N")
                return
            # Если нода есть, то сериализуем её
            res.append(str(node.val))

            # Обходим левое дерево
            dfs(node.left)
            # Обходим правое дерево
            dfs(node.right)

        # Запускаем рекурсию
        dfs(root)

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')

        self.i = 0

        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()