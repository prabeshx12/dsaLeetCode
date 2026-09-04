class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
    