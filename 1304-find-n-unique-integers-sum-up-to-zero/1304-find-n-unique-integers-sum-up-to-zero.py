class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        total = 0
        for i in range(1, n + 1):
            if i == (n):
                res.append(total)
            else:
                res.append(-i)
                total += i

        return res