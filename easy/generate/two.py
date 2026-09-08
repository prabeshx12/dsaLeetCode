class Solution():
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):
            rowlist = [1] * (i + 1)

            for j in range(1, i):
                rowlist[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(rowlist)

        return triangle
