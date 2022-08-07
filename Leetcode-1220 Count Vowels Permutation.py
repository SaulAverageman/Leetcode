class Solution:
    def countVowelPermutation(self, n: int) -> int:
        nex=[[2],[1,3],[1,2,4,5],[3,5],[1]]
        di=[1,1,1,1,1]
        
        for i in range(n-1):
            di2=[0,0,0,0,0]
            for k in range(5):
                for e in nex[k]:
                    di2[int(e)-1]+=di[k]
            di=di2
        out=0
        for k in range(5):
            out+=di[k]
        return out%1000000007
