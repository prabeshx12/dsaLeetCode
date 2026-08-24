class Solution(object):
    def lengthOfLastWord(self, s):
        # without the split
        fast = len(s) - 1

        while fast >= 0 and s[fast] == " ":
            fast -= 1

        count = 0

        while fast >= 0 and s[fast] != " ":
            count += 1
            fast -= 1

        return count
