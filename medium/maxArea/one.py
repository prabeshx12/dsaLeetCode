class Solution(object):
    def maxArea(self, height):
        """
        The logic is simple go through the array and if difference in the height of the two points are smaller,
        use that smaller height and multiply that with the gap between them and check for the maximum area.
        It is not optimal for now as time limit gets exceeded for larger n. But works fine for small n.
        """
        maxim = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                if i != j:
                    if height[i] <= height[j]:
                        area = (j - i) * height[i]
                    else:
                        area = (j - i) * height[j]

                if area > maxim:
                    maxim = area

        return maxim
