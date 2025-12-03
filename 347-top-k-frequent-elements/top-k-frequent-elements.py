from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        freq_count=Counter(nums)
        top_k = [item for item, count in freq_count.most_common(k)]
        return top_k