class Solution(object):
    def countBits(self, n):
        """
        The logic is Dynamic Programming say we want to know for the number 101(i.e. 5),
        what I can do is split 10 | 1 so that I know 10's count earlier and count that last bit.
        """
        return_list = [0] * (n + 1)

        for i in range(1, n + 1):
            return_list[i] = return_list[i >> 1] + (i & 1)

        return return_list
