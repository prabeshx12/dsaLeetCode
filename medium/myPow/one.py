class Solution(object):
    def myPow(self, x, n):
        """
        The logic is that to reduce the number of multiplications to logn, what we can do is keep squaring unless
        n is odd and then multiply that with the result. for n < 0 we can swap the x to 1/x and n to -n.
        """
        if n < 0:
            x = 1 / x
            n = - n

        result = 1.0

        while n != 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result
