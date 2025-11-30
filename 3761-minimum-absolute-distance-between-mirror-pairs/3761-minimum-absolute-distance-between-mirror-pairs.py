class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mirror = {}

        res = float('inf')
        for i, num in enumerate(nums):
            if num in mirror:
                res = min(res, i - mirror[num])
            s = str(num)
            s = int(s[::-1])
            mirror[s] = i

        if res == float('inf'):
            return -1
        return res