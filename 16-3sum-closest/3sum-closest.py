class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        s=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if abs(target-total)< abs(target-s):
                    s=total
                if total==target:
                    return target 
                elif total<target:
                    left+=1
                else:
                    right-=1
        return s


        