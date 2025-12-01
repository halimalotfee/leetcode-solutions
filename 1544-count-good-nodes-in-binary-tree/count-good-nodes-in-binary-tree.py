# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
    
        def counting(node,maxi):
            if not node:
                return 0
            if node.val>=maxi:
                good=1
            else: good=0
            new_max=max(maxi,node.val)
            return good+counting(node.left,new_max)+counting(node.right,new_max)
        return counting(root,root.val)