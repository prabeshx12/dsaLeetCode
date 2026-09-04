class Solution(object):
    def reverseString(self, stringtext):
        reverseNum = ''
        
        for i in range(len(stringtext) - 1, -1, -1):
            reverseNum += stringtext[i]

        return reverseNum
