class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        aliceSum=sum(aliceSizes)
        bobSum=sum(bobSizes)
        mi=(aliceSum+bobSum)//2
        for i in aliceSizes:
            num=mi-(aliceSum-i)
            if num in bobSizes:
                resultat=[i,num]
                return resultat

        