class Solution(object):
    def fib(self, n):
        """
        The logic is to just use the definition of fibonacci i.e. required number is sum of previous two numbers
        """
        a = 0; b = 1

        for _ in range(n):
            c = a + b
            a = b
            b = c
        
        return a
