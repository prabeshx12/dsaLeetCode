class Solution(object):
    def groupAnagrams(self, strs):
        """
        The logic here is to first get the hashMap of individual words and then only based on the matched hashmaps
        group those words together. Note: this is not optimal approach.
        """
        returnList = []
        finalList = []
        rList = []


        for string in strs:
            hashMap = {}
            for j in string:
                hashMap[j] = hashMap.get(j, 0) + 1
            returnList.append([string, hashMap])

        for _, h1 in returnList:
            if h1 not in finalList:
                finalList.append(h1)

        for h in finalList:
            group = []
            for stri, h2 in returnList:
                if h == h2:
                    group.append(stri)
            rList.append(group)

        return rList
