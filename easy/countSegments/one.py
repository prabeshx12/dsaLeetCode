class Solution(object):
    def countSegments(self, s):
        """
        The logic is to check for the non space character and also to check if i == 0 i.e. the first
        char or before (i - 1)th index char to be equal to space character. In those cases, we increment the count.
        """
        count = 0

        for i in range(len(s)):
            if s[i] != " " and (i == 0 or s[i - 1] == " "):
                count += 1

        return count
