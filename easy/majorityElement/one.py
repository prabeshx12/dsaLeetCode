class Solution(object):
    def majorityElement(self, nums):
        """
        The logic here is to build hashMap and check if any of the number frequency is greater than floor of
        n / 2; if so return the val else keep checking. It is not so optimal as space complexity is O(n).
        """
