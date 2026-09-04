class Solution(object):
    def isPowerOfTwo(self, n):
        """
        The logis is similar to that of the Brian Kernighan's Algorithm, The power of two have only 1 set bit.
        So, if we subtract the number with 1 and & with the number then result is zero if n > 0.
        """
        return n > 0 and (n & (n - 1)) == 0
        