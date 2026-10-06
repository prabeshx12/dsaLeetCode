class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        The logic is the simple hashMap search for the letters present in the ransomNote are present in the magazine
        if so then we return true else we return false.
        """
        hashMap = {}

        for i in range(len(magazine)):
            hashMap[magazine[i]] = hashMap.get(magazine[i], 0) + 1

        for char in ransomNote:
            if char in hashMap:
                hashMap[char] -= 1
                if hashMap[char] < 0:
                    return False

            else:
                return False

        return True