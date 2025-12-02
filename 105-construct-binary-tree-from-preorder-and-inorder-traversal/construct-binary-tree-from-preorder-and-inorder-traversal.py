# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        
        if not preorder or not inorder :
            return None
        root_val=preorder[0]
        root = TreeNode(root_val)

        root_indx=inorder.index(root_val)
        root.left=self.buildTree(preorder[1:root_indx+1],inorder[:root_indx])
        root.right=self.buildTree(preorder[root_indx+1:],inorder[root_indx+1:])
        return root