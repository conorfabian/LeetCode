class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [1] * len(nums)
        prod = 1
        for i, num in enumerate(nums):
            pre[i] = prod
            prod *= num

        post = [1] * len(nums)
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = prod
            prod *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i])

        return res