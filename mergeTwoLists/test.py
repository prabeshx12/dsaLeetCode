class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3

head = node1
current = head

node4 = ListNode(25)

# say I want to insert 25 then;
while current is not None:
    if current.next.val >= node4.val >= current.val:
        node4.next = current.next
        current.next = node4
        break
    
    current = current.next

current = head

while current is not None:
    print(current.val)
    current = current.next