class Solution(object):
    def missingNumber(self, nums):
        """

        """
        sum_num = 0
        for num in nums:
            sum_num += num
        
        f_sum = int(len(nums)/2 * (len(nums) + 1))

        return f_sum - sum_num


sol = Solution()
print(sol.missingNumber([3, 0, 1]))