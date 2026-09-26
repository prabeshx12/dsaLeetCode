class Solution(object):
    def hammingDistance(self, x, y):
        """
        The logic is to just take the last bit of the numbers x and y and XOR the result. If it was 1 then count will
        increase else it won't. We then rotate the x and y towards the right.
        """
        count = 0
        
        while x or y:
            count += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        
        return count
