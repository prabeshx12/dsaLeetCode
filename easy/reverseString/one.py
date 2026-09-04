#Two pointer approach
class Solution(object):
    def reverseString(self, stringtext):
        a = 0; b = len(stringtext) - 1
        string = list(stringtext)

        while a < b:
            string[a], string[b] = string[b], string[a]
            a += 1
            b -= 1
            
        return ''.join(string)
