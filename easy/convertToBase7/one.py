class Solution(object):
    def convertToBase7(self, num):
        """
        The idea is to approach this through common conversion on the base such as binary, octal or hex format. For 
        negative ones we just append the negative sign.
        """
        if num == 0:
            return "0"
        
        sign = -1 if num < 0 else 1
        num = abs(num)
        result = []

        while num:
            result.append(str(num % 7))
            num //= 7
        
        if sign == -1:
            return "-" + "".join(result[::-1])
        else:
            return "".join(result[::-1])
