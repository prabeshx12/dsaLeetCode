class Solution(object):
    def maxArea(self, height):
        """
        The logic here is to reduce the convention of seeing everyline down to O(n). This can be done by 
        using the two pointers; left and right. We find the width and as we go down the line, move the
        left pointer to increase the chance of hitting the bigger area, due to the fact that width will
        decrease no matter moving the left or right pointer, but the minimum height might get increased.
        """
        left = 0; right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_area = max(max_area, width * min_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
