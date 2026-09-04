class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            result = digits[i] + 1
            if result >= 10:
                digits[i] = int(str(result)[-1])
            else:
                digits[i] = result
                return digits
            
        if int(str(result)[0]) == 1:
            return [1] + digits
