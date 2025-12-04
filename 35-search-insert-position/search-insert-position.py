class Solution(object):
    def searchInsert(self, nums, target):
        i=0 
        while i<len(nums):
            if nums[i]==target:
                return i 
            if target<nums[i]:
                return i
            i+=1
        return len(nums)
        