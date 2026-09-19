class Solution(object):
    def majorityElement(self, nums):
        """
        The logic is to use the Boyer-Moore algorithm. Think of that as something like different number cancels
        out the one occurence of the current candidate, but since majority element appera more than n / 2,
        it cannot be completely canceled out. That is the principle behind the Boyer-Moore algorithm.
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                
            count = count + 1 if candidate == num else count - 1

        return candidate
    