class Solution(object):
    def findTheDifference(self, s, t):
        """
        The logic here is to XOR the ASCII numbers of the string of s and t combined and result is the only 
        string that is different. So we can convert it back to ASCII. The Space Complexity here is just O(1)
        instead of O(k).
        """
        result = 0

        for char in s + t:
            result ^= ord(char)

        return chr(result)
