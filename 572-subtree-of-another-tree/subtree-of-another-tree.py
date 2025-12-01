# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def Same(a,b):
            if not a and not b :
                return True
            if not a or not b:
                return False
            if a.val != b.val:         
               return False
            return Same(a.left, b.left) and Same(a.right, b.right)
                    
        if not subRoot:
            return True
        if not root:
            return False

        if Same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
