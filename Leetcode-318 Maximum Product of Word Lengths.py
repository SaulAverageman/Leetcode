class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ll=[]
        
        for e in words:
            ll.append(set(e))
        
        out=0
        for i in range(len(ll)-1):
            for j in range(i+1,len(ll)):
                if len(ll[i])+len(ll[j])==len(ll[i].union(ll[j])):
                    out=max(out,len(words[i])*len(words[j]))
        return out