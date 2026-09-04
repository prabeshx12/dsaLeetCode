class Solution(object):
    def maxSubArray(self, nums, window_size):
        sub_arr = sum(nums[:window_size])
        max_subsum = sub_arr

        for i in range(window_size, len(nums)):
            sub_arr += nums[i] - nums[i - window_size]
            max_subsum = max(sub_arr, max_subsum)
            
        return max_subsum
