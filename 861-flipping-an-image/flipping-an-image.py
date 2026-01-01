class Solution(object):
    def flipAndInvertImage(self, image):
        res=[]
        for row in image:
            flipping=row[::-1]
            inverting=[1 if a==0 else 0  for a in flipping]
            res.append(inverting)
        return res 