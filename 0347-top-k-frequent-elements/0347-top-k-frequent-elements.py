class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        frequency = [[] for i in range(len(nums))]

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for val in counts:
            frequency[counts[val] - 1].append(val)

        results = []
        i = len(nums) - 1
        while k != 0:
            for num in frequency[i]:
                if k == 0:
                    break
                results.append(num)
                k -= 1
            i -= 1

        return results