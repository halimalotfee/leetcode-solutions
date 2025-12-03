class Solution(object):
    def permute(self, nums):
        path=[]
        result=[]
        def backtrack():
            if len(path)==len(nums):
                result.append(path[:])
                return 

            for c in nums:
                if c not in path:
                    path.append(c)
                    backtrack()
                    path.pop()
        backtrack()
        return result 
        