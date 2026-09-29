class Solution(object):
    def isIsomorphic(self, s, t):
        """
        The logic is to use the two hashmaps, as isomorphic means two way one-to-one mapping between the characters.
        So we check the mapping and if it differs then return False, else return True.
        """
        hashMap1 = {}
        hashMap2 = {}

        for a, b in zip(s, t):
            if a in hashMap1 and hashMap1[a] != b:
                return False
                
            if b in hashMap2 and hashMap2[b] != a:
                return False
            
            hashMap1[a] = b
            hashMap2[b] = a
        
        return True
    