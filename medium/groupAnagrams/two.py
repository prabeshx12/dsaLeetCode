class Solution(object):
    def groupAnagrams(self, strs):
        """
        The logic here is to sort the individual words to get their key and use those keys to group strings
        """
        hashMap = {}

        for word in strs:
            key = "".join(sorted(word))
            
            if key in hashMap:
                hashMap[key].append(word)
            else:
                hashMap[key] = [word]

        return hashMap.values()
