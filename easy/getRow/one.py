class Solution(object):
    def getRow(self, rowIndex):
        """
        The logic is to just build the final row with the reverse index in the second loop.
        and then adding that second loop variable with the variable - 1's value that way we create the
        intended row values of the pascal's triangle. Space Complexity will be O(rowIndex) instead of
        O(rowIndex ^ 2)
        """
        row = [1]

        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0 , -1):
                row[j] += row[j - 1]

            row.append(1)

        return row
