class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        
        for c in s:
            seen.add(c)

        return len(seen)