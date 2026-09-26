class Solution(object):
    def toHex(self, num):
        """
        This is only for the positive number hex calculation based on the mapping of the numbers from 10 to 15
        with a to f and dividing the number and getting remainders add up in the reverse. For negative numbers
        however this doesn't work.
        """
        hashMap = {}
        result = ''

        for val, key in enumerate("abcdef", 10):
            hashMap[val] = key

        while num != 0:
            result += hashMap.get(num % 16, str(num % 16))
            num //= 16
        
        return result
