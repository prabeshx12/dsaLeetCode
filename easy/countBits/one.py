class Solution(object):
    def countBits(self, n):
        """
        The logic is to just make the range start from 1 to n and count each letters 1 using the
        Brian Kernighan's Algorithm.
        """
        list_bin = [0]
        
        for i in range(1, n + 1):
            count = 0

            while i != 0:
                count += 1
                i &= (i - 1)
                
            list_bin.append(count)

        return list_bin
