class Solution(object):
    def majorityElement(self, nums):
        candidate=None
        count=0
        for a in nums:
            if count==0:
                candidate=a 
            if a==candidate:
                count+=1
            else: 
                count-=1
        return candidate 