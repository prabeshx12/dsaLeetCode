class Solution(object):
    def longestPalindrome(self, s):
        """
        This is the improved version of the brute-force that we did in the one.py i.e. we don't check substrings
        shorter than the current longest palindrome. The complexity is still O(n ^ 3) but we avoided substrings
        shorter ones than the current ones.
        """
        longest = ""

        for start in range(len(s)):
            for end in range(start + len(longest), len(s) + 1):
                sub = s[start:end]

                if sub == sub[::-1]:
                    longest = sub

        return longest
