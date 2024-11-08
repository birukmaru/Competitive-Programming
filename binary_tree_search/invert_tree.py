class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=val
        self.right=right
        
class Solution:
    def invertTree(self,root:TreeNode)-> TreeNode:
        if not root:
            return None
        temp=root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
print(self.invertTree([1,2,3]))