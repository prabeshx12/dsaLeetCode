# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        The logic is the binary search version to minimize the calls of API, if mid is the badversion then right 
        side numbers from mid + 1 are rejected; else left will go to mid + 1. and when left < right throws false,
        we return the left.
        """
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
