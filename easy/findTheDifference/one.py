class Solution(object):
    def findTheDifference(self, s, t):
        """
        We create hashMap and map the number of letter frequency. In the second loop,
        subtract the frequency based on the presence of the second string (t) letter matching that in the first
        string. If letter is not in the hashMap or letter frequency goes to negative then return that specific
        letter. 
        """
        hashMap = {}
        
        for i in s:
            hashMap[i] = hashMap.get(i, 0) + 1

        for j in t:
            if j in hashMap:
                hashMap[j] -= 1

                if hashMap[j] < 0:
                    return j
            else:
                return j
