class Solution(object):
    def climbStairs(self, n):
        """
        The solution is found based on this logic:
        Either the last step will be 1 or 2; 
        If 1, then, they need to climb climbStairs(n - 1) steps
        and if 2, then, they need to climb climbStairs(n - 2) steps.
        Together, we have climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2), which is the fibonacci sequence.
        """
        if n <= 1:
            return 1

        a = 1
        b = 1

        for i in range(1, n):
            test = a + b
            a = b
            b = test

        return b
        