class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        result=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
                if nums1[i]==nums2[j]:
                    if not result or result[-1]!=nums1[i]:

                        result.append(nums2[j])
                    j+=1
                    i+=1
                elif nums1[i] < nums2[j]:
                   i+=1
                else: 
                    j+=1
        return result
                    

        