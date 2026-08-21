class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            temp = x
            rev = 0
            while x != 0:
                rem = x % 10
                rev = rev * 10 + rem
                x //= 10
            return rev == temp