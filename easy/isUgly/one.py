class Solution(object):
    def isUgly(self, n):
        """
        The logic is to just loop through 2, 3 and 5 and divide the numbers by those numbers
        until we have the remainder zero, at last we compare if n is 1. If it is 1 then it will be
        ugly as only factors will be those in [2, 3, 5] else it will not be ugly.
        """
        if n <= 0:
            return False
        
        for fact in [2, 3, 5]:
            while n % fact == 0:
                n //= fact

        return n == 1
