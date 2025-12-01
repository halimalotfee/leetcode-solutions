# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):

        
        def retrier(node):
            if not node:
                return []
            return retrier(node.left)+[node.val]+retrier(node.right)

        new_root=retrier(root)
        return new_root[k-1]
           


    
        