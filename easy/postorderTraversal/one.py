# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        The idea is to use the iterative approach for the postorder but with the trick related to reversing the
        preorder i.e. first traversing Node -> Right -> Left and reversing the final traversal order which gives
        Left -> Right -> Node which is our Post Order Traversal in Binary Search Tree.
        """
        node = root
        stack = []
        order = []

        while stack or node:
            while node:
                stack.append(node)
                order.append(node.val)
                node = node.right
            
            node = stack.pop()
            node = node.left
        
        return order[::-1]
