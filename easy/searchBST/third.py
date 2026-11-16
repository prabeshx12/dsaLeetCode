# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def searchBST(self, root, val):
        """
        The idea is to use the iterative approach of the property of the BST.
        """
        if not root:
            return None
        
        node = root

        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            else:
                node = node.right

        return None
