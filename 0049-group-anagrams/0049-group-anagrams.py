class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)

        return anagrams.values()