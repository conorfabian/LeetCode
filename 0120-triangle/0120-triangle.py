class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        def combine_rows(lower_row, upper_row):
            return [upper + min(lower_left, lower_right)
                    for upper, lower_left, lower_right in
                    zip(upper_row, lower_row, lower_row[1:])]
        return reduce(combine_rows, triangle[::-1])[0]