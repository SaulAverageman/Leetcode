class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return 0
        s1=" "+s1
        s2=" "+s2
        l1,l2,l3=len(s1),len(s2),len(s3)
        arr=[[0 for e in s2] for e in s1]
        
        arr[0][0]=1
        
        for i in range(l1):
            for j in range(l2):
                if i==0 and j==0:
                    continue
                k=i+j-1
                a=0
                if s3[k]==s1[i]:
                    a=arr[i-1][j]
                
                b=0
                if s3[k]==s2[j]:
                    b=arr[i][j-1]
                
                arr[i][j]=a or b
        return arr[-1][-1]
