# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        The logic is to use iterative approach than recursive due to the recursive solutions being trivial.
        Among the inorder, preorder and the postorder only thing that matters while solving the iterative approach
        is how you connect this approach with recursive as "where do you append the root node in the order?" is the only
        thing that matters.
        """
        node = root
        stack = []
        order = []

        while stack or node:
            while node:
                stack.append(node)
                order.append(node.val)
                node = node.left
            
            node = stack.pop()
            node = node.right
        
        return order
