class Solution(object):
    def longestPalindrome(self, s):
        """
        This is the most optimal for the longestPalindrome with the complexity of O(n ^2) and space of O(1). The idea
        is to expand outward from each possible center of either odd or even length palindrome.
        """
        longest = ""

        for i in range(len(s)):
            # Odd-length palindrome
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]

                left -= 1
                right += 1

            # Even-length palindrome
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]

                left -= 1
                right += 1

        return longest
