class Solution(object):
    def isPowerOfTwo(self, n):
        """
        Checking at the setbit, if that is 1 number of 1s and n > 0, then that number is power of 2.
        i.e. 4 = 100, 4 > 0; 8 = 1000, 8 > 0
        """
        if n < 0:
            return False

        count = 0

        while n != 0:
            n &= (n - 1)
            count += 1

        if count == 1:
            return True
        else:
            return False
