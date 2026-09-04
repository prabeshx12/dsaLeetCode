class Solution(object):
    def hammingWeight(self, n):
        """
        This algorithm is known as Brian Kernighan's Algorithm which removes the rightmost set bit of the number
        and we count until we get zero. Hence the complexity is O(number of 1s) not O(number of bits).
        """
        count = 0

        while n:
            n &= n - 1
            count += 1

        return count
    