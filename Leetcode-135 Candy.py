class Solution:
    def candy(self, ratings: List[int]) -> int:
        q=[]
        arr=[0]*len(ratings)
        
        for i in range(len(ratings)):
            q.append([ratings[i],i])
        
        q.sort()
        
        out=0
        for x in q:
            a,b=0,0
            i=x[1]
            if i>0:
                if ratings[i]>ratings[i-1]:
                    a=arr[i-1]
            if i<len(arr)-1:
                if ratings[i]>ratings[i+1]:
                    b=arr[i+1]
            
            arr[i]=max(a,b)+1
            out+=arr[i]
        return out
        
        
