class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=int(s[:k],2)
        col=set()
        col.add(n)
        BIG=2**(k-1)
        BIG2=2*BIG
        for i in range(k,len(s)):
            n-=int(s[i-k])*BIG
            n+=n
            n+=int(s[i])
            col.add(n)
            if len(col)==BIG2:
                return 1
        return len(col)==BIG2