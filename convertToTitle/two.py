class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        Changing the Excel 1-26 to python 0-25 for mapping and then taking remainder and finding the letter
        along with the number integer division with base 26.
        """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = ""

        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            title = letters[remainder] + title
            columnNumber //= 26

        return title


sol = Solution()
print(sol.convertToTitle(2601))