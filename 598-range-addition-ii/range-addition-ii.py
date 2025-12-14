class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return m*n
        min_row=m
        min_col=n
        for a ,b in ops:
            min_row=min(a,min_row)
            min_col=min(b,min_col)
        return min_row*min_col
        