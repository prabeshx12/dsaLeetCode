class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        The logic is to start from the position with the first head element not equal to val so skip unless 
        head's value is not equal to val. Then after that we track two pointers current and previous.
        if current node val is equal to required, then previous.next = current.next and current = current.next
        else; we just move the previous and the current pointers ahead.
        """
        while head and head.val == val:
            head = head.next

        current = head
        final_head = head
        previous = current

        while head is not None:
            if head.val == val:
                previous.next = current.next
            else:
                previous = current

            current = current.next

        return final_head
