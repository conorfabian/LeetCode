class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = "0"
        sum = 0

        for num in str(n):
            if num != "0":
                x += num
                sum += int(num)

        return int(x) * sum