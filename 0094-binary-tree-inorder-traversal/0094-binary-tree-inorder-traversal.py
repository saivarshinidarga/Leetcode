# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        st=[]
        Curr=root
        while Curr or st:
            while Curr:
                st.append(Curr)
                Curr=Curr.left
            Curr=st.pop()
            res.append(Curr.val)
            Curr=Curr.right
        return res
        