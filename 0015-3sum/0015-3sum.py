class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        nums = sorted(nums)
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val > 0:
                    r -= 1
                elif val < 0:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

        return res