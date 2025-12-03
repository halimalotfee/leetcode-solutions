class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def backtrack(s='',open=0,close=0):
            if len(s)==n*2:
                res.append(s)
                return res
            if open<n:
               backtrack(s+'(',open+1,close)

            if close<open :
                backtrack(s+')',open,close+1)
        backtrack()
        return res
