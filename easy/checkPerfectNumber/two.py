class Solution(object):
    def checkPerfectNumber(self, num):
        """
        The logic is to go through the condition of i <= sqrt(num) as we know the divisors come in pairs. i.e. if i 
        evenly divides num then num // i also divides num evenly. So we go through that loop until that condition of
        i <= sqrt(num).
        """
        if num <= 1:
            return False

        sum_factors = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                sum_factors += i

                if i != num // i:
                    sum_factors += num // i

            i += 1

        return sum_factors == num
