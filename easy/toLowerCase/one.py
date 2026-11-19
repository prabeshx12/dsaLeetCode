class Solution(object):
    def toLowerCase(self, s):
        """
        The idea is to check the ord of the character in s. If it is capital i.e. in the range of 65 to 90 we add
        the 32 to get their respective lower case characters.
        """
        lower = ''

        for char in s:
            if 65 <= ord(char) <= 90:
                lower += chr(ord(char) + 32)
            else:
                lower += char
        
        return lower
