class Solution(object):
    def isPerfectSquare(self, num):
        """
        The logic is the binary search implementaion and we know that square of num is not greater than
        half of the num.
        """
        if num < 2:
            return True

        left = 1
        right = num // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
