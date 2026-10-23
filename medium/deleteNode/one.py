class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        The logic is to delete the given node from a singly-linked list without accessing the head of the list. 
        The given node is guaranteed not to be the last node.
        """
        node.val = node.next.val
        node.next = node.next.next