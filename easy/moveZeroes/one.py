class Solution(object):
    def moveZeroes(self, nums):
        """
        The logic is to use two variables one fast for the loop, another to track the swapping place on 
        where to swap. If number is non zero, do the swapping and increment that track variable to store
        the next swapping case, else just continue. We don't return here as we just change it inplace.
        """
        track = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[track], nums[fast] = nums[fast], nums[track]
                track += 1
