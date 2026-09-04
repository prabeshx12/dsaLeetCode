# This code is for O(n) complexity as O(nlogn) can be done by sorting the hashMap.
class Solution:
    def topKFrequent(self, nums, k):
        returnList = []
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for key, freq in hashMap.items():
            bucket[freq].append(key)

        for freq in range(len(nums), 0, -1):
            for num in bucket[freq]:
                returnList.append(num)

                if len(returnList) == k:
                    return returnList
