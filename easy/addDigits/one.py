class Solution(object):
    def addDigits(self, num):
        """
        The logic is to check the each final sum of the digits' length whether it is not 1, until that loop it
        with the steps and when the length is 1, return the digit.
        """
        while len(str(num)) != 1:
            result = 0
            list_nums = []
            
            while num != 0:
                list_nums.append(num % 10)
                num //= 10

            for num in list_nums:
                result += num

            num = result

        return num
        