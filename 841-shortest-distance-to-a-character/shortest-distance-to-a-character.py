class Solution(object):
    def shortestToChar(self, s, c):
        n=len(s)
        res=[0]*n
        left_res=float('-inf')
        for i in range(n):
            if s[i]==c:
                left_res=i
            res[i]=i-left_res
        right_res=float('inf')
        for i in range(n-1,-1,-1):
            if s[i]==c:
               right_res=i
            res[i]=min(res[i],right_res-i)
        return res

        
