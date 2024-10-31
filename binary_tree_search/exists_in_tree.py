def existsInTree(root,value):
    if root is None:
        return False
    else:
        inLeft=existsInTree(root.left,value)
        inRight=existsInTree(root.right,value)
        return root.data == value or inLeft or inRight