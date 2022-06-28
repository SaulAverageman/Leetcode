class Solution:
    def minDeletions(self, s: str) -> int:
        arr=[0]*26
        
        for e in s:
            arr[ord(e)-97]+=1
        
        for i in range(26):
            if arr[0]!=0:
                arr.append(arr[0])
            arr.pop(0)
        
        arr.sort(reverse=True)
        
        s=set()
        out=0
        for e in arr:
            while e!=0 and e in s:
                out+=1
                e-=1
            
            if e!=0:
                s.add(e)
        return out
