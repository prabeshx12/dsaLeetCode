class Solution(object):
    def rLE(self, s):
        """
        This is the helper function for handling the Run Length Encoding
        """
        if not s:
            return ""

        listOne = []
        slow = 0
        count = 1
        
        for fast in range(1, len(s)):
            if s[slow] != s[fast]:
                listOne.append(str(count) + s[slow])
                slow = fast
                count = 1
            else:
                count += 1

        listOne.append(str(count) + s[slow])

        return "".join(listOne)

    def countAndSay(self, n):
        """
        The logic here is to generate the nth term of the Count and Say sequence.
        """
        base = "1"

        while n > 1:
            base = self.rLE(base)
            n -= 1
        
        return base
