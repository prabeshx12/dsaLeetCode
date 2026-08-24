class Solution(object):
    def lengthOfLastWord(self, s):
        # using split() makes this problem easy through removing of the spaces and easily selectin the last word through indexing
        listOne = s.split()
        lastWord = listOne[-1]
        count = 0
        
        for i in lastWord:
            if i:
                count += 1

        return count