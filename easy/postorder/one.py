"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        The idea is similar to the of the postorder only difference lies in the sequence we follow i.e. in case of
        post order we go through the children first and then we process the root recursively.
        """
        result = []

        def dfs(node):
            if not node:
                return

            for child in node.children:
                dfs(child)
            
            result.append(node.val)
        
        dfs(root)
        return result
