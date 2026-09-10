# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        The logic is to create a new linked list for the final answer and go through the linked list till one of them
        is non empty and add the result and add new node i.e. new_node. if one of them is None i.e. completed then we 
        create new node and since its default is zero, it just adds 0; and at last if the longer linked list is completed
        and has carry extra that extra new_node value is set to 1, else previous.next is set to None to cut off that
        redundant node.
        """
        final = ListNode()
        dummy = final
        carry = 0

        while l1 is not None or l2 is not None:
            dum_node = ListNode()
            if l1 is None:
                l1 = dum_node
            elif l2 is None:
                l2 = dum_node

            result = l1.val + l2.val + carry

            if result >= 10:
                dummy.val = result % 10
                carry = 1
            else:
                carry = 0
                dummy.val = result

            previous = dummy

            new_node = ListNode()
            dummy.next = new_node
            dummy = dummy.next

            l1 = l1.next
            l2 = l2.next

        if carry == 1:
            dummy.val = 1
        else:
            previous.next = None

        return final


# Linked List One
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3


# Linked List Two
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node4.next = node5
node5.next = node6

# Setting the heads
head1 = node1
head2 = node4

sol = Solution()
result_head = sol.addTwoNumbers(head1, head2)


# The result
while result_head is not None:
    print(result_head.val)
    result_head = result_head.next