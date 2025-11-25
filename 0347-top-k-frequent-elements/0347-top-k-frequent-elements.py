class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        frequencies = [[] for i in range(len(nums) + 1)]
        for num, count in counts.items():
            frequencies[count].append(num)

        res = []
        for freq in frequencies[::-1]:
            if k <= 0:
                break
            elif freq:
                for num in freq:
                    res.append(num)
                    k -= 1

        return res