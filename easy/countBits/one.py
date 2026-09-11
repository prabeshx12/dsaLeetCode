class Solution(object):
    def countBits(self, n):
        """
        
        """
        list_bin = []
        for i in range(n + 1):
            count = 0
            if i == 0:
                list_bin.append(0)

            while i & (i - 1) != 0:
                count += 1
            list_bin.append(count)

        return list_bin