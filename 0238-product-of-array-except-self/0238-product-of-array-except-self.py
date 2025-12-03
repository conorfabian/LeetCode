class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [1] * len(nums)
        product = 1
        for i, num in enumerate(nums):
            pre[i] = product
            product *= num

        suf = [1] * len(nums)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            suf[i] = product
            product *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * suf[i])

        return res