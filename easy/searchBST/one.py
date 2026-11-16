# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def searchBST(self, root, val):
        """
        The idea is to use the inOrder traversal of the general binary tree and go through each and every node
        comparing the values to find the value if not return None.
        """
        if not root:
            return None
        
        stack = [root]
        node = root

        while stack:
            while node:
                stack.append(node)

                if node.val == val:
                    return node
                
                node = node.left
        
            node = stack.pop()
            node = node.right
        
        return None
