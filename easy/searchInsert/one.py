class Solution(object):
    def searchInsert(self, nums, target):
        """
        The logic is to just us the binary search, but instead don't check the mid to target,
        just check if it is greater or not, based on the condition if less increase left with
        mid + 1, else do right to mid and return left as that will be the index.
        """
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
