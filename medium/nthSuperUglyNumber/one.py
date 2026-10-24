class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        The logic is to check every number starting from 2 and checking the numbers factor with the primes; if
        they match we append and continue till we find the nth one. It is not optimal for bigger n as it checks
        all the numbers starting from 2.
        """
        if n == 1:
            return 1
        
        sup_ugly = [1]
        num = 2

        while 1:
            temp = num

            for j in primes:
                while temp % j == 0:
                    temp //= j
            if temp == 1:
                sup_ugly.append(num)
                if len(sup_ugly) >= n:
                    return num
                
            num += 1
