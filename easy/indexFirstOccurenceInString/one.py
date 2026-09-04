class Solution(object):
    def indexFirstOccurenceInString(self, needle, haystack):
        n = len(needle)
        h = len(haystack)

        for fast in range(h - n + 1):
            if needle == haystack[fast:n + fast]:
                return fast

        return -1
    