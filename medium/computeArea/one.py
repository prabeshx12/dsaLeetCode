class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        The logic here is to first, calculate the individual areas of both rectangles and add them.
        Then, find the boundaries of their intersection using max() for the left and bottom edges,
        and min() for the right and top edges.

        If the left edge is >= the right edge, or the bottom edge is >= the top edge, the rectangles 
        do not overlap with positive area, so the overlapped area is zero. Otherwise, calculate the 
        intersection area and subtract it from the total to avoid counting it twice.
        """
        rect1 = (ax2 - ax1) * (ay2 - ay1)
        rect2 = (bx2 - bx1) * (by2 - by1)
        total = rect1 + rect2

        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)
        cx2 = min(ax2, bx2)
        cy2 = min(ay2, by2)

        if cx1 >= cx2 or cy1 >= cy2:
            overlapped = 0
        else:
            overlapped = (cx2 - cx1) * (cy2 - cy1)

        return total - overlapped
