class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        The logic is to just keep the numbers which are not in the nums in the returnlist after iterating through
        all numbers in that range of length of that numbers (len(nums)) exclusive.
        """
        set1 = set(nums)
        returnList = []

        for num in range(1, len(nums) + 1):
            if num not in set1:
                returnList.append(num)

        return returnList
