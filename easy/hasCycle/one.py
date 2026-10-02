class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        The logic is the floyd Cycle algorithm where we assign two pointers, i.e. fast and slow. slow moves one
        step at a time while fast moves 2 steps at a time. If fast hits null there is no cycle, and if fast catches
        up with the slow then there is the cycle in the linkedlist.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
        