class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3

list1 = node1

# for adding 5, 25 and 40 we have:
node4 = ListNode(5)
node5 = ListNode(25)
node6 = ListNode(40)

node4.next = node1 # for first node
list1 = node4

node5.next = node3 # for second node
node2.next = node5

node3.next = node6 # for third node

current = list1

while current is not None:
    print(current.val)
    current = current.next
