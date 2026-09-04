class Solution(object):
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        rev = 0
        y = abs(x)

        while y != 0:
            a = y % 10
            rev = rev * 10 + a
            y //= 10

        if len(bin(rev)[2:]) >= 32:
            return 0
        else:
            return sign * rev
