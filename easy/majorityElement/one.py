class Solution(object):
    def majorityElement(self, nums):
        """
        The logic here is to build hashMap and check if any of the number frequency is greater than floor of
        n / 2; if so return the val else keep checking. It is not so optimal as space complexity is O(n).
        """
        hashMap = {}

        for val in nums:
            hashMap[val] = hashMap.get(val, 0) + 1

            if hashMap[val] > len(nums) // 2:
                return val
        