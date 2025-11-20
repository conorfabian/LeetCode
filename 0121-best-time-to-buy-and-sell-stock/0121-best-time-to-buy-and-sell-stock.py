class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 0
        res = float("-inf")

        while r < len(prices):
            res = max(res, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1

        return res