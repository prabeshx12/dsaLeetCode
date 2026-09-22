class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        The logic is to convert the linkedlist values to string and the do the two pointer string check;
        if they don't equal, return False else after complete run return True.
        """
        string = ''
        curr = head

        while curr is not None:
            string = string + str(curr.val)
            curr = curr.next

        left = 0; right = len(string) - 1

        while left < right:
            if string[left] == string[right]:
                left += 1; right -= 1
            else:
                return False
            
        return True