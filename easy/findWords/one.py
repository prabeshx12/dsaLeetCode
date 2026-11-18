class Solution(object):
    def findWords(self, words):
        """
        The idea here is to first store the row of the first character of the word and then check whether
        other characters come from the same row or not. We here make use of the for .. else such that whenever we hit
        break we won't append it to the returnlist. Only when the function runs without break will we append the 
        word in the returnlist.
        """
        firstrow = "qwertyuiop"
        secondrow = "asdfghjkl"
        thirdrow = "zxcvbnm"
        returnlist = []

        def samerow(char):
            if char in firstrow:
                return 1
            elif char in secondrow:
                return 2
            elif char in thirdrow:
                return 3
        
        for word in words:
            isrow = samerow(word[0].lower())
            
            for char in range(1, len(word)):
                if isrow != samerow(word[char].lower()):
                    break
            else:
                returnlist.append(word)
        
        return returnlist   
                