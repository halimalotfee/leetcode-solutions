class Solution(object):
    def getRow(self, rowIndex):
        row=[1]
        for i in range(1,rowIndex+1):
            row=[0]+row
            for j in range(i):
                row[j]=row[j]+row[j+1]
        return  row
        
        