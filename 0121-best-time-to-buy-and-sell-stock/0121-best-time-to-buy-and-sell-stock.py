class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        res = float('-inf')

        for i in range(len(prices)):
            res = max(res, prices[i] - prices[l])
            if prices[i] < prices[l]:
                l = i

        return res