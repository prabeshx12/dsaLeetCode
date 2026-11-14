class Solution(object):
    def arrangeCoins(self, n):
        """
        The idea here is to only increase the count when the sum of terms upto k is less than or equal to n; if its
        greater than we stop the iteration.
        """
        k = 1; count = 0

        while k * (k + 1) // 2 <= n:
            count += 1
            k += 1
        
        return count
