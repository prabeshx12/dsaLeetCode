# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        The idea is to make use of the helper isMirror and check for the right or left subtrees and based on that 
        return the result.
        """
        def isMirror(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return (isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))

        return isMirror(root.left, root.right) if root else True
