class Solution(object):
    def grayCode(self, n):
        """
        Recursively generate the Gray Code sequence for n - 1 bits. Keep the previous sequence as the first half.
        Then reverse the previous sequence and add its length (2^(n-1)) to each element to set the new leading bit.
        Reversing ensures that the transition between the two halves differs by only the new leading bit. 
        Adding the same offset to every element preserves the one-bit difference property within the second half.
        """
        if n == 0:
            return [0]
        else:
            prev = self.grayCode(n - 1)
            return prev + [x + len(prev) for x in prev[::-1]]
