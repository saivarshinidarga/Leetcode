# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        self.i = 0
        def helper(bound):  
            if self.i < len(preorder) and preorder[self.i] < bound:
                root = TreeNode(preorder[self.i])
                self.i+= 1
                root.left = helper(root.val)
                root.right = helper(bound)
                return root
                
        return  helper(float("inf"))
