class Solution:
    def is_fact(self, n):
        if n == 0:
            return 1
        else:
            return n * self.is_fact(n - 1)

    def generate(self, numRows):
        """
        The logic here is factorial driven and is using the combinations formula for the constants, i.e.
        nCr.
        """
        list1 = []
        for i in range(numRows):
            list2 = []
            for j in range(i + 1):
                list2.append(int(self.is_fact(i)/(self.is_fact(j) * self.is_fact(i - j))))
            list1.append(list2)

        return list1


sol = Solution()
print(sol.generate(4))