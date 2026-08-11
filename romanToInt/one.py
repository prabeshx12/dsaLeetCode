class Solution(object):
    def romanToInt(self, romanString):
        dictMap = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000,
        }
        finalInt = 0

        for key in range(len(romanString)):
            # format is "if condition_that_can_be_false" and "condition that might crash"; last one is never evaluated in python
            if key + 1 < len(romanString) and dictMap[romanString[key]] < dictMap[romanString[key + 1]]:
                finalInt -= dictMap[romanString[key]]
            else:
                finalInt += dictMap[romanString[key]]
                
        return finalInt
