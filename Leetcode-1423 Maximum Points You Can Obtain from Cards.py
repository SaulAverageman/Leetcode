class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        for i in range(1,len(cardPoints)):
            cardPoints[i]+=cardPoints[i-1]
        
        cardPoints.insert(0,0)
        
        out=-1
        
        for i in range(k+1):
            out=max(out,cardPoints[i]+cardPoints[-1]-cardPoints[i-k-1])
        return out
