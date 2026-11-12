"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        The idea is to use dfs as helper inside the function and recursively go through the child i.e. first
        process(node) and then the children.
        """
        result = []

        def dfs(node):
            if not node:
                return

            result.append(node.val)

            for child in node.children:
                dfs(child)

        dfs(root)
        return result
