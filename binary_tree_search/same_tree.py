def isSameTree(p,q):
    if not p and q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return (isSameTree(p.left,q.left) and
    isSameTree(p.right,q.right))