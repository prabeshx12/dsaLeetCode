class Solution(object):
    def wordPattern(self, pattern, s):
        """
        The logic here is to map each letter of the pattern to the single word of string making sure that
        there is one-one mapping in between the letters of the pattern and words of the string both ways, making
        sure that no word of the string is left unmapped, i.e. it should be bijective.
        """
        liststring = s.split(" ")
        hashMap = {}

        if len(pattern) != len(liststring):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashMap:
                if liststring[i] in hashMap.values():
                    return False
                hashMap[pattern[i]] = liststring[i]
            else:
                if hashMap[pattern[i]] != liststring[i]:
                    return False
            
        return True
