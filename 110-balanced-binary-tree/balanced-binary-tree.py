# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
         
        def heightTree(node):
            if not node:
               return 0
            LeftHeight=heightTree(node.left)
            if LeftHeight==-1:
                return -1
                        
            RightHeight=heightTree(node.right)
            if RightHeight==-1:
                return -1
            if abs(LeftHeight-RightHeight)>1:
                return -1
            return max(LeftHeight,RightHeight)+1
        return heightTree(root)!=-1

        