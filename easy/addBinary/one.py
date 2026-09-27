class Solution(object):
    def addBinary(self, a, b):
        """
        The logic is related to the summation and carry bits of the two bits when a carry is there;
        summation will be a XOR b XOR c and carry will be ab + bc + ca. Based on that we first reverse the bits to
        start from the 0th index and for the smaller bit check if the index is valid if invalid then assign zero to
        the bit.
        """
        new_a = a[::-1]
        new_b = b[::-1]

        if len(a) >= len(b):
            longBit = new_a; shortBit = new_b
        else:
            longBit = new_b; shortBit = new_a

        carry = 0
        summation = 0
        result = []

        for i in range(len(longBit)):
            bit1 = int(shortBit[i]) if i < len(shortBit) else 0
            bit2 = int(longBit[i])
            summation = carry ^ bit1 ^ bit2
            carry = bit1 & bit2 | bit1 & carry | bit2 & carry
            result.append(str(summation))
        
        if carry:
            result.append('1')

        return ''.join(result)[::-1]
