class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vals = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in vals:
                return [i, vals[diff]]
            vals[nums[i]] = i