class Solution(object):
    def subsets(self, nums):
        result=[]
        subsets=[]
        def create_sub(i):
            if i==len(nums):
                result.append(subsets[:])
                return
            subsets.append(nums[i])
            create_sub(i+1)
            subsets.pop()
            create_sub(i+1)
        create_sub(0)
        return result


            
        