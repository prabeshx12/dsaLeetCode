class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        The logic is to subtract the ASCII value of the character to that of A to get the index in python
        and add 1 to get the index for the excel. For each result we accumulate i.e. multiply by 26 and add 
        that value.
        """
        result = 0

        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value

        return result
            