class Solution(object):
    def singleNumber(self, nums):
        """
        The logic here is to use two bitmasks, ones and twos, to track how many times each bit has appeared, modulo 3.

        - ones stores bits that have appeared once.
        - twos stores bits that have appeared twice.

        For each number:
        1. Update ones using XOR to toggle bits and use ~twos to remove bits that have already appeared twice.
        2. Update twos using XOR and use ~ones to remove bits that have already appeared once after the update.

        When a bit appears for the third time, it is removed from both ones and twos. Therefore, bits belonging to numbers
        appearing three times cancel out, leaving the unique number in ones.
        """
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones
