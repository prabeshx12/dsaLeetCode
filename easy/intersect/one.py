class Solution(object):
    def intersect(self, nums1, nums2):
        """
        The logic here is to create two hashMaps and then check if the key of 1st hashmap is present in the hashmap 2nd.
        If it is then check if count is same of that key if that is same print until the frequency of that key reaches 0.
        Similarly if that value of key is less or greater depending upon the hashmap1's value then we print the smaller one
        frequency i.e. append in the return List.
        """
        returnList = []
        hashMap1 = {}
        hashMap2 = {}

        for num in nums1:
            hashMap1[num] = hashMap1.get(num, 0) + 1
        
        for num in nums2:
            hashMap2[num] = hashMap2.get(num, 0) + 1
        
        for key, value in hashMap1.items():
            if key in hashMap2:
                if hashMap2[key] >= value:
                    while value != 0:
                        returnList.append(key)
                        value -= 1
                
                elif hashMap2[key] < value:
                    while hashMap2[key] != 0:
                        returnList.append(key)
                        hashMap2[key] -= 1
        
        return returnList
