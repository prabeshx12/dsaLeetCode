# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        The idea here is to use stack to track the nodes and push to the stack only the left childrens if the node
        has no right or left child and is a part of left subtree then we sum that value.
        """
        stack = []
        summ = 0

        if not root:
            return 0

        stack.append((root, False))

        while stack:
            node, isLeft = stack.pop()

            if not node.left and not node.right:
                if isLeft:
                    summ += node.val
            
            if node.right:
                stack.append((node.right, False))
            
            if node.left:
                stack.append((node.left, True))

        return summ
