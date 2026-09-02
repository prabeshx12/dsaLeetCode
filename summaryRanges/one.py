class Solution(object):
    def summaryRanges(self, nums):
        """
        The logic is to have 2 variables for the starting and ending of the range;
        "start" as the starting point and "slow" as the ending point.
        We loop through the var "fast" to check if nums[slow] + 1 != nums[fast] if that is the case 
        then we append the range's, first, in a separate list else continue to increase the "slow".
        After we get to the final loop and it gets completed, we have to again append for the remaining
        elements as slow didn't reach the len(nums) - 1 value for the final range of values. That is the
        append for that final range.
        """
        slow = start = 0
        range_list = []
        final_list = []

        for fast in range(1, len(nums)):
            if nums[slow] + 1 != nums[fast]:
                range_list.append([nums[start], nums[slow]])
                start = fast
            slow += 1

        range_list.append([nums[start], nums[slow]])
        
        for a, b in range_list:
            if a == b:
                final_list.append(str(a))
            else:
                final_list.append(str(a) + "->" + str(b))

        return range_list
