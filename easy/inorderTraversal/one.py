# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        The logic is to use the iterative approach for the inorder traversal of the tree.
        """
        node = root
        stack = []
        order = []

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            print(node.val)
            order.append(node)
            node = node.right

        return order
