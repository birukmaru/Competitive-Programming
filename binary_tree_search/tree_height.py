def treeHeight(root):
    if root is None:
        return 0
    else:
        leftHeight=treeHeight(root.left)
        rightHeight=treeHeight(root.right)
        return 1 + max(leftHeight,rightHeight)
    