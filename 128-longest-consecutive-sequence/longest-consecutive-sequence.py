class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
           return 0 

        nums=sorted(list(set(nums)))
        k=1
        lenght=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1 :
                k+=1
                lenght=max(lenght,k)
            else:
                k=1
        return lenght   
  