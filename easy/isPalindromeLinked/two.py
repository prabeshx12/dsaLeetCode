class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        The logic is to find the middle of the linked list using slow & fast pointers and then make the
        reverse linkedlist form the middle and compare each of those values.
        """
        if head is None or head.next is None:
            return True

        # for finding the middle node
        slow = head; fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # prev is now head of the reversed second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # now comparing both
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
