class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen.keys():
                return (seen[compliment], i)
            else:
                seen[nums[i]] = i
