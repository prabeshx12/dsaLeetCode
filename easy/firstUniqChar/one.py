class Solution(object):
    def firstUniqChar(self, s):
        """
        The logic is to create a hashmap for the frequency of the elements, and then return the frequency of the
        first element with the value of 1, if not then return -1.
        """
        hashMap = {}
        
        for i in range(len(s)):
            hashMap[s[i]] = hashMap.get(s[i], 0) + 1
        
        for j in range(len(s)):
            if hashMap[s[j]] == 1:
                return j
        
        return -1 
