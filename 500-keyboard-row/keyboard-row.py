class Solution(object):
    def findWords(self, words):
        res=[]
        first_row=set("qwertyuiop")
        second_row=set("asdfghjkl")
        third_row=set("zxcvbnm")
        for word in words:
            w=set(word.lower())
            if w<=first_row or w<=second_row or w<=third_row:
                res.append(word)
        return res
        