# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        diametre=[0] 
        def height(node):
            if not node:
                return -1 
            hl= height(node.left)
            hr=height(node.right)
            diametre[0] = max(diametre[0], hl + hr + 2)
            return 1 + max(hl, hr)
        height(root)
        return diametre[0]
            