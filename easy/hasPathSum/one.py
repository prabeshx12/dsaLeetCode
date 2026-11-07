# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        The logic is to use recursive DFS to explore all possible root-to-leaf paths. At each node, we subtract
        its value from the targetSum and pass the remaining sum to its left and right children. If we reach a
        leaf node, we check whether its value equals the remaining targetSum. We return True if either the left
        or right subtree contains a valid root-to-leaf path. If the node is None, we return False.
        """
        if root is None:
            return False

        if root.left is None and root.right is None:
            return targetSum == root.val

        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining) or
            self.hasPathSum(root.right, remaining)
        )
