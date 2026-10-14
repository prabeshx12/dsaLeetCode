class Solution(object):
    def grayCode(self, n):
        """
        Generate n-bit Gray Code by XORing each integer with itself right-shifted by one bit, ensuring consecutive 
        values differ by exactly one bit.
        """
        return [i ^ (i >> 1) for i in range(1 << n)]
