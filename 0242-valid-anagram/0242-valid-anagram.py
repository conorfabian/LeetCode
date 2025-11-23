class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1, t1 = {}, {}

        for c in s:
            s1[c] = 1 + s1.get(c, 0)

        for c in t:
            t1[c] = 1 + t1.get(c, 0)

        return s1 == t1