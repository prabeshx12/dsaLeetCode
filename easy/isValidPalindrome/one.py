class Solution(object):
    def isPalindrome(self, s):
        """
        The logic is to continue updating the a or b unless we hit the alnum character. If they are same we 
        do nothing. If they are not same then we return False. If there are no any alnum character then,
        one of the pointer gets skipped till it finds the alnum or we hit the condition a < b and we get
        the result based on that if condition.
        """
        a = 0
        b = len(s) - 1
        
        while a < b:
            while not s[a].isalnum() and a < b:
                a += 1

            while not s[b].isalnum() and a < b:
                b -= 1

            if s[a].lower() != s[b].lower():
                return False

            a += 1; b -= 1
        
        return True
