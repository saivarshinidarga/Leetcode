# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def helper(root,low,high):
            if root is None:
                return True
            if low<root.val < high:
               return (helper(root.left,low,root.val)
                     and helper(root.right,root.val,high))
            else:
                return False
        return helper(root,float("-inf") ,float("inf"))
