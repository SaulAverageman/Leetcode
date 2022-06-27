class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x=0
        t=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                t+=1
                if s1[i]=='x':
                    x+=1
        if t%2==1:
            return -1
        
        out=x//2+(t-x)//2
        t-=2*out
        return out+t
