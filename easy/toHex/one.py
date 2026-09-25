class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hashMap = {}
        result = ''

        for val, key in enumerate("abcdef", 10):
            hashMap[val] = key

        while num != 0:
            result += hashMap.get(num % 16, str(num % 16))
            num //= 16
        
        return result
