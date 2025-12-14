class Solution(object):
    def distributeCandies(self, candyType):
        n=len(candyType)/2
        candyTypes=list(set(candyType))
        res=min(n,len(candyTypes))
        return res
        