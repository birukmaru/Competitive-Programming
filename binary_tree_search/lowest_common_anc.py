def lowestCommonAnc(root,p,q):
    cur=root
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur=cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur=cur.left
        else:
            return cur