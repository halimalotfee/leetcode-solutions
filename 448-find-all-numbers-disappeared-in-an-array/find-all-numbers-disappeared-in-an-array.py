class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        nums_set = set(nums)
        result = []
        
        for i in range(1, n + 1):
            if i not in nums_set:
                result.append(i)
        
        return result