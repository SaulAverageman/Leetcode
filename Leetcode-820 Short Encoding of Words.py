class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        di={}
        for e in words:
            if e[-1] in di:
                di[e[-1]].append(e)
            else:
                di[e[-1]]=[e]
        
        def task(arr):
            arr.sort(key=lambda x:-len(x))
            
            ll=[]
            out=0
            for e in arr:
                k=0
                for ee in ll:
                    if ee[len(ee)-len(e):]==e:
                        k=1
                        break
                if k==0:
                    out+=1
                    ll.append(e)
                    out+=len(e)
            return out
        out=0
        for k in di:
            out+=task(di[k])
            
        return out
