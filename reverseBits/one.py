class Solution(object):
    def reverseBits(self, n):
        """
        Logic is to first find the remainders in log2(n) complexity in order so reverse
        bits will be captured and append them to the list.
        The loop then, through them afteradding them will find the resulting decimal number.
        """
        binList = []
        result = 0
        
        while n > 0:
            rem = n % 2
            binList.append(rem)
            n //= 2
        
        pad_length = 32 - len(binList)
        pad_list = pad_length * [0]
        binList = binList + pad_list
        
        for i in range(len(binList) - 1, -1, -1):
            result = result + 2 ** i * binList[len(binList) - 1 - i]
        
        return result
