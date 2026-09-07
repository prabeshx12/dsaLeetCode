class Solution(object):
    def isHappy(self, n):
        """
        The logic is to have the list for the already squared digits sum number if numbers are not in the list then
        keep appending else number is not happy. If n == 1, then the number is happy.
        """
        list_ranges = [n]

        while n != 1:
            sq_sum = 0

            while n != 0:
                sq_sum += (n % 10) ** 2
                n //= 10
            
            if sq_sum not in list_ranges:
                list_ranges.append(sq_sum)
                n = sq_sum
            else:
                return False
        
        return True
        