class Solution(object):
    def intersection(self, nums1, nums2):
        """
        The logic is to make a hashMap for just unique numbers having value as 1. Then in the next loop we scan
        through second arrray if that number is in nums2, if it is, then, we append(j) and make that dict value
        of j = 0
        """
        dictMap = {}
        result = []

        for i in nums1:
            dictMap[i] = 1

        for j in nums2:
            if j in dictMap and dictMap[j]:
                result.append(j)
                dictMap[j] = 0

        return result
