class Solution(object):
    def rotate(self, nums, k):
        """
        The logic is to use another list initialized to zero and do the circular index assignment to the specific index
        of the nums. That way the new list will be formed based on the rotation key k applied.
        """
        length = len(nums)
        returnList = [0] * length

        for index in range(length):
            returnList[(index + k) % length] = nums[index]
        
        return returnList
