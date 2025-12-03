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

        frequencies = [[] for i in range(len(nums))]
        for key, count in counts.items():
            frequencies[count-1].append(key)
        print(frequencies)

        res = []
        for frequency in frequencies[::-1]:
            for num in frequency:
                res.append(num)
                k -= 1
            if k <= 0:
                break

        return res