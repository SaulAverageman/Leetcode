class Solution:
    def longestPalindrome(self, s: str) -> str:
        s2=s[::-1]
        self.req=[0,0]
        def ss(i,n):
            if n%2==0:
                self.req=[i-n//2+1,i+n//2+1]
            else:
                self.req=[i-n//2,i+n//2+1]
        l1=len(s)+1
        ll=[[0 for i in range(l1)] for j in range(l1)]
        out=0

        for i in range(1,l1):
            for j in range(1,l1-i+1):
                if j==l1-i:
                    ll[i][j]=ll[i-1][j-1]+1
                elif s2[i-1]==s[j-1]:
                    ll[i][j]=ll[i-1][j-1]+2

                if ll[i][j]>out and (i+j==l1 or i+j+1==l1):
                    out=ll[i][j]
                    ss(j-1,ll[i][j])
            #print(ll[i])

        return s[self.req[0]:self.req[1]]
