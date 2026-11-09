# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        The idea is to use iterative approach but without reversing the order as we track the last_visited node
        and based on that we find whether we are finished both childern of the node or not.
        """
        stack = []
        order = []
        last_visited = None
        node = root

        while stack or node:

            if node:
                stack.append(node)
                node = node.left

            else:
                peek = stack[-1]

                if peek.right and last_visited != peek.right:
                    node = peek.right
                else:
                    order.append(peek.val)
                    last_visited = stack.pop()

        return order
