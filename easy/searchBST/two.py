# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def searchBST(self, root, val):
        """
        The idea is to use the property of the BST i.e. to search only the subtree based on the value of the node
        and the goal value using recursion.
        """
        if not root:
            return None
        
        node = root

        if node.val == val:
            return node
        
        elif node.val > val:
            return self.searchBST(node.left, val)
        
        else:
            return self.searchBST(node.right, val)
