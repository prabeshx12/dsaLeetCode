class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        The logic is to first find the length of the linked list, then subtract the n to get the node to remove
        from the first in index. After that if index which is length - n = 0 then, return curr.next which is None.
        Else use previous to store the current and move the current to current.next. 
        At last strip the connection as prev.next = current.next and current.next = None.
        """
        curr1 = curr2 = head
        prev = curr2
        length = 0

        while curr1 is not None:
            length += 1
            curr1 = curr1.next

        index = length - n

        if index == 0:
            return head.next

        while index != 0:
            prev = curr2
            curr2 = curr2.next
            index -= 1

        prev.next = curr2.next
        curr2.next = None

        return head
