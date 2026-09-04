class Solution(object):
    def deleteDuplicates(self, head):
        """
        The logic is to first compare head value with the previous if same then skip
        else do the dummy.next as the head and finally do the dummy's next to None.
        """
        final = ListNode()
        dummy = final
        prev = None

        while head is not None:
            if head.val != prev:
                dummy.next = head
                dummy = dummy.next
                prev = head.val
            head = head.next

        dummy.next = None
        return final.next
