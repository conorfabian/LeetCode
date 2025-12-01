class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, num in enumerate(numbers):
            diff = target - num
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                m = ((r - l) // 2) + l
                if numbers[m] < diff:
                    l = m + 1
                elif numbers[m] > diff:
                    r = m - 1
                else:
                    return [i+1, m+1]