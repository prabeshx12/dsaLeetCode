class Solution(object):
    def fib(self, n):
        """
        The logic here is to use recursion for solving it since fib(n) = fib(n - 1) + fib(n - 2) from
        recurrence relations.
        """
        if n == 0:
            return 0
        
        elif n == 1:
            return 1
        
        else:
            return self.fib(n - 1) + self.fib(n - 2)
