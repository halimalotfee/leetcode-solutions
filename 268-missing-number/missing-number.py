class Solution(object):
    def missingNumber(self, nums):
        n= len(nums)
        missing=n
        for i , num in enumerate(nums):
            missing^=i^num
        return missing
        