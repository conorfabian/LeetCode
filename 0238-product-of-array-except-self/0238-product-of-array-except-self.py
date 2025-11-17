class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [1] * len(nums)
        suf = [1] * len(nums)

        preSum = 1
        for i in range(len(nums)):
            pre[i] = preSum
            preSum *= nums[i]

        sufSum = 1
        for i in range(len(nums) - 1, -1, - 1):
            suf[i] = sufSum
            sufSum *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * suf[i])

        return res