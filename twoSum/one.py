class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen.keys():
                return (seen[compliment], i)
            else:
                seen[nums[i]] = i

sol = Solution()
listOne = [1, 2, 3, 4, 5, 6, 7]
targetOne = 11
print(sol.twoSum(listOne, targetOne))