class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=[0]*26
        m=len(s)
        n=len(t)
        if m!=n:
            return False
        for i in range(m):
            j=ord(s[i])-97
            l[j]+=1
        for i in range(n):
            j=ord(t[i])-97
            l[j]-=1
        has_nonzero = any(x != 0 for x in l)
        return not has_nonzero
        