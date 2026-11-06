# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        The idea is to store each node alongside its corresponding depth in the stack and keep updating 
        the maximum depth encountered. When backtracking, restore the node's depth from the stack.
        """
        node = root
        stack = []
        counter = 0
        maxx = 0

        while stack or node:
            while node:
                counter += 1
                stack.append((node, counter))
                maxx = max(maxx, counter)
                node = node.left

            node, counter = stack.pop()
            node = node.right

        return maxx
