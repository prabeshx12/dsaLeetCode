class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length

        if k != 0:
            nums[:] = nums[-k:] + nums[:-k]

        return nums
