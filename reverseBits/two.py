class Solution(object):
    def reverseBits(self, n):
        """
        The logic here is to shift the result bits left and then append it with the last bit of the n
        and progressively right shift the n till the 32th loop.
        """
        result = 0

        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result
