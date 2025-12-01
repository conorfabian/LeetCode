class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for c in s: # ord(c) - ord('a')
                key = ord(c) - ord('a')
                counts[key] += 1
            hashMap[tuple(counts)].append(s)

        res = []
        for key in hashMap:
            res.append(hashMap[key])

        return res