class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        The logic is to use 3 pointers and do the assignment based on the node connection breakage.
        """
        curr = head
        prev = None

        while curr is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
