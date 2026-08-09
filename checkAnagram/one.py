class Solution(object):
    def checkAnagram(self, string1, string2):
        dictOne = {}
        if len(string1) != len(string2):
            return False
        
        for i in string1:
            dictOne[i] = dictOne.get(i, 0) + 1

        for j in string2:
            if j in dictOne:
                dictOne[j] -= 1
                if dictOne[j] < 0:
                    return False
            else:
                return False

        return True
