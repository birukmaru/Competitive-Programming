from collections import Counter
def findAnagrams(s,p):
    result=[]
    target_count=collections.Counter(p)
    windows_count=collections.Counter(s[:len(p)-1])


