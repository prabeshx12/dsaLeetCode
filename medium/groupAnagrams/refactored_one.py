class Solution(object):
    def groupAnagrams(self, strs):
        """
        The logic here is to just use tuple as the keys for sorted charmap and appending them to hashmap[keys]
        based on whether they match those keys or not.
        """
        hashmap = {}

        for string in strs:
            charMap = {}

            for char in string:
                charMap[char] = charMap.get(char, 0) + 1

            key = tuple(sorted(charMap.items()))

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(string)

        return list(hashmap.values())