class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        The logic is to check whether head or head.next is None if it is then return the head. Now for the
        recursion part we assign the new_head and call the reverselist with passing head as head.next.
        We assign head.next.next to be head so that the connection is reversed and the previous connection
        is broken using None assignment.
        """
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head
