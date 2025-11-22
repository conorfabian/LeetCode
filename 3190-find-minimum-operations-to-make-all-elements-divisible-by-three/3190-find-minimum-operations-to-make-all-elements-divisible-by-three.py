class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # is the array sorted?
        # can it contain negative numbers?
        # optimize of time or space complexity?
        # any array size or numerical constraints?

        # [] => 0
        # [-9, -7] => 1

        # brute force: iterate through and check how far each number is from a number divisible by 3. TC: O(n), SC: O(1)
        
        res = 0

        for num in nums:
            val = num % 3
            if val != 0:
                res += 1

        return res