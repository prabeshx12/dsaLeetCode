class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        The logic is to take two variables count and max_count, and go through the nums loop; in each step 
        comparing whether it is 1 or 0. If 1 then increase count else assign max_count with the max of the count
        and the max_count while resetting the count. At last we return the max of the current count and max_count,
        for any latest max count.
        """
        count = 0
        max_count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        
        return max(max_count, count)
