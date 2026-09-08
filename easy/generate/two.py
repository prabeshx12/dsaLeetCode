class Solution():
    def generate(self, numRows):
        """
        The logic is to append the list of 1s first in the row and then in the middle add the previous row 
        columns starting from the 1st to the 2nd last, hence the range (1, i).
        """
        triangle = []

        for i in range(numRows):
            rowlist = [1] * (i + 1)

            for j in range(1, i):
                rowlist[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(rowlist)

        return triangle
