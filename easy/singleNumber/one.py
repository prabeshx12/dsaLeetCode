class Solution(object):
    def singleNumber(self, nums):
        """
        If O(n) space was allowed; I could have gone with the hashMap or the hashSet i.e.
        hashMap: make hashMap and then return the key with the value == 1
        hashSet: add/remove the elements that are duplicate and then remove the last element(i.e. pop)
        But for the optimal O(1) then there should be bit manipulation so XOR is the key.
        """
        result = 0

        for num in nums:
            result ^= num

        return result
