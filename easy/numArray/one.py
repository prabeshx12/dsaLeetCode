class NumArray(object):

    def __init__(self, nums):
        """
        The logic here is to use the concept of prefix sum which will reduce the call of sumRange to O(1).
        The prefix sum will store the sum of first i elements and subtracting the left index from the right + 1
        will give the sum.
        """
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)