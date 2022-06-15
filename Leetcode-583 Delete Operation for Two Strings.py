class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)+1
        l2 = len(word2)+1
        
        ll=[[0 for i in range(l2)] for i in range(l1)]
        
        for i in range(1,l1):
            for j in range(1,l2):
                if word1[i-1]==word2[j-1]:
                    ll[i][j]=ll[i-1][j-1]+1
                else:
                    ll[i][j]=max(ll[i-1][j],ll[i][j-1])
        return l1+l2-2-2*ll[-1][-1]
        
