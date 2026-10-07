class Solution(object):
    def myAtoi(self, s):
        """
        The logic is to first skip the leading whitespace, then check for the immediate sign of the string,
        if that is present there we keep the value of sign in sign vairable. Then for each string char if
        that is digit then we build that number. Also checking the boundary conditions and presenting the 
        result based on that boundary.
        """
        skip = 0
        n = len(s)

        # Skip leading spaces
        while skip < n and s[skip] == " ":
            skip += 1

        # Sign
        sign = 1
        
        if skip < n and s[skip] == "+":
            skip += 1
        elif skip < n and s[skip] == "-":
            sign = -1
            skip += 1

        # Build number
        num = 0

        while skip < n and s[skip].isdigit():
            num = num * 10 + int(s[skip])
            skip += 1

        num *= sign

        # 32-bit signed integer limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
