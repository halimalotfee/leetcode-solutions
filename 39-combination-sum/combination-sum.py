class Solution(object):
    def combinationSum(self, candidates, target):
        result=[]
        def Backtrack(remain,idx,path):
            if remain==0:
                result.append(path[:])
                return 
            if idx==len(candidates) or remain<0:
                return 
            path.append(candidates[idx])
            Backtrack(remain-candidates[idx],idx, path)
            path.pop()
            Backtrack(remain, idx+1,path)
        Backtrack(target, 0,[])
        return result

            
