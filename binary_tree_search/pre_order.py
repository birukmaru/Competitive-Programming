"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def dfs(nod):
            if not nod:
                return 
            res.append(nod.val)

            for i in nod.children:
                dfs(i)
        dfs(root)
        return res
