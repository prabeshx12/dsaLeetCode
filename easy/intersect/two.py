class Solution(object):
    def intersect(self, nums1, nums2):
        """
        The more optimal solution here would be to make the first hasmap of nums1 and then go through the digits of the
        nums2 and check if the count of num of num2 in the hashmap of 1st list is zero if that is then we won't append,
        else we append until we hit 0.
        """
        hashmap = {}
        output = []

        for num in nums1: 
            hashmap[num] = hashmap.get(num, 0) + 1

        for num in nums2: 
            if hashmap.get(num, 0) != 0:
                output.append(num)
                hashmap[num] -= 1

        return output
