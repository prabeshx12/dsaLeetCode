class Solution(object):
    def containsDuplicate(self, nums):
        """
        The logic is simple so as to compare the lengths of normal list and the set of that nums as sets won't
        contain duplication and will result in fewer lengths than the nums in case of duplication, with the 
        condition, len(set) <= len(nums)
        """
        return len(nums) != len(set(nums))