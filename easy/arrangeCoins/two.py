import math

class Solution(object):
    def arrangeCoins(self, n):
        """
        For solving this in the O(1) time we use the quadratic formula and solve for k which will be 
        k = (sqrt(8n + 1) - 1) / 2
        """
        return (math.isqrt(8 * n + 1, 0.5) - 1) // 2
