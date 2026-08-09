class Solution(object):
    def checkAnagram(self, string1, string2):
        dictOne = {}
        dictTwo = {}
        if len(string1) != len(string2):
            return False
        
        for i in string1:
            dictOne[i] = dictOne.get(i, 0) + 1

        for j in string2:
            dictTwo[j] = dictTwo.get(j, 0) + 1

        return dictOne == dictTwo
