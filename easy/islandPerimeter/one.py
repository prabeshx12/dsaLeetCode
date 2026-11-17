class Solution(object):
    def islandPerimeter(self, grid):
        """
        The idea here is to check in each cell whether there is land to the up/left, if there is then subtract 2.
        we could do the one subtraction and check all edges but that would not be optimal. So we check the up and left
        instead of all edges.
        """
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4

                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
                
        return perimeter
