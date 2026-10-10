class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        The logic is to convert the nums list to set and then the range of the numbers of that n integer to set
        and take the difference between the sets and convert it back to the list.
        """
        set1 = set(nums)
        set2 = set(list(range(1, len(nums) + 1)))

        return list(set2 - set1)
