class Solution(object):
    def addBinary(self, a, b):
        """
        The logic is related to the summation and carry bits of the two bits when a carry is there;
        summation will be a XOR b XOR c and carry will be ab + bc + ca. Based on that we assign to pointers,
        i and j which will be the length of numbers - 1 and then move those pointers. This way we don't need
        to find the longBit or shortBit as we can loop until the condition i >= 0 or j >= 0 or carry.
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            bit1 = int(a[i]) if i >= 0 else 0
            bit2 = int(b[j]) if j >= 0 else 0

            summation = carry ^ bit1 ^ bit2
            carry = bit1 & bit2 | bit1 & carry | bit2 & carry
            
            result.append(str(summation))

            i -= 1; j -= 1

        return ''.join(result)[::-1]
