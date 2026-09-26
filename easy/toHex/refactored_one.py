class Solution(object):
    def toHex(self, num):
        """
        The logic here is for negative numbers we use their r's complement, i.e. for base 16 it will be r = 16.
        For small n since 32 bit is used each 4 bit represents hex, so 32/4 = 8 is the n here. Then we subtract
        the absolute number of n, to gets its r's complement. Then, the number goes through the same pipeline as that
        of the positive integers.
        """
        hashMap = {}
        result = ''

        if num == 0:
            return "0"

        if num < 0:
            num = 16 ** 8 - (num * -1) # as num is negative so

        for val, key in enumerate("abcdef", 10):
            hashMap[val] = key

        while num != 0:
            result = hashMap.get(num % 16, str(num % 16)) + result
            num //= 16
        
        return result
