class Solution(object):
    def convertToBase7(self, num):
        """
        The idea is similar just we use the string instead of list.
        """
        if num == 0:
            return "0"
        
        n = abs(num)
        result = ""

        while n:
            result += str(n % 7)
            n //= 7
        
        if num < 0:
            result += "-"

        return result[::-1]
