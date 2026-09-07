class Solution(object):
    def missingNumber(self, nums):
        """
        The logic is to subtract the formula of the sum n*(n+1)/2 of the range of numbers to the given
        list sum and subtract it with the formulat one.
        """
        sum_num = 0
        for num in nums:
            sum_num += num
        
        f_sum = int(len(nums)/2 * (len(nums) + 1))

        return f_sum - sum_num


sol = Solution()
print(sol.missingNumber([3, 0, 1]))