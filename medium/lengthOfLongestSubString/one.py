class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        The idea is to use list for this and use sliding window to keep track of the unique characters.
        """
        seen = []
        length = 0
        
        for i in range(len(s)):
            while s[i] in seen:
                seen.pop(0)
            
            seen.append(s[i])

            if len(seen) > length:
                length = len(seen)
        
        return length
