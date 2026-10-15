class Solution(object):
    def rotate(self, nums, k):
        """
        The logic is to first reduce k modulo the length of the list so that rotations greater than the
        list length are handled correctly. If k is not zero, we rotate the list to the right by k positions by 
        concatenating the last k elements (nums[-k:]) with the remaining elements (nums[:-k:]). The slice assignment 
        nums[:] updates the original list in place.
        """
        length = len(nums)
        k = k % length

        if k != 0:
            nums[:] = nums[-k:] + nums[:-k]

        return nums
