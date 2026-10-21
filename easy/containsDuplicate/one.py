class Solution(object):
    def containsDuplicate(self, nums):
        """
        The logic is the simple hashmap with value equal to True depending on the new nums in the list. If again
        the new num is seen we return False as that indicates duplication. Else we append that num in hashmap.
        """
        hashMap = {}

        for num in nums:
            if num in hashMap:
                return True
            else:
                hashMap[num] = True
        
        return False
