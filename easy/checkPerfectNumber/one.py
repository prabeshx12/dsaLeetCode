class Solution(object):
    def checkPerfectNumber(self, num):
        """
        The logic is here is to just go up to the num // 2 + 1 and check for each digit if that is evenly divisible to
        that number; if so then we add those numbers to the sum_factors and if the final result is equal to that original
        number then we return true else we return false. But this method is not efficient.
        """
        sum_factors = 0

        for i in range(1, num // 2 + 1):
            if num % i == 0:
                sum_factors += i
        
        return sum_factors == num
