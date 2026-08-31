class Solution(object):
    def hammingWeight(self, n):
        """
        This algorithm checks every bit and compares the final bit; if that is 1 it increments
        counter else bits are shifted towards the right. But this is not optimized as the complexity
        is: O(number of bits)
        """
        
        count = 0

        while n != 0:
            if n & 1:
                count += 1
            n >>= 1
        
        return count
