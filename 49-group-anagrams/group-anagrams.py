from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):  
        anagramlist = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagramlist[sorted_word].append(word)
        return list(anagramlist.values())


