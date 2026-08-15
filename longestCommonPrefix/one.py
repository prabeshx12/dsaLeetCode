class Solution(object):
    def longestCommonPrefix(self, strs):
        minStr = min(strs, key=len) # finds the minimum string based on the length
        lengthMin = len(minStr)

        #for .. else was new for me; else gets excecuted only when the inner loop finishes without any break.
        for i in range(lengthMin, -1, -1):
            for j in strs:
                if minStr[:i] != j[:i]:
                    break
            else:
                return minStr[:i]
        return ""
            
