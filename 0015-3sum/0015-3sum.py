class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        
        nums.sort()
        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in results:
                        results.append([nums[i], nums[l], nums[r]])
                    l += 1

        return results