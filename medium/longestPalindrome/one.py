class Solution(object):
    def longestPalindrome(self, s):
        """
        The idea here is to go through each and every substring, reverse it and compare it with itself for the
        palindrome. The complexity is O(n^3) here.
        """
        longest = ""

        for start in range(len(s)):
            rev = ""
            
            for index in range(len(s)):
                rev = s[start:len(s) - index][::-1]

                if rev == s[start:len(s) - index]:
                    longest = max([longest, rev], key = len)
        
        return longest
