# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        The idea is the traversal through each nodes and if either one of them is empty at any point return False.
        Also returning False if node values are different. Else if condition passes then we return True. We append
        nodes two times so we pop their respective nodes and handle them separately.
        """
        stack = []

        while stack or p or q:
            while p or q:
                if p and not q:
                    return False
                elif not p and q:
                    return False
                
                if p.val == q.val:
                    stack.append(q)
                    stack.append(p)

                    p = p.left
                    q = q.left
                else:
                    return False
                    
            p, q = stack.pop(), stack.pop()
            p = p.right
            q = q.right
        
        return True
