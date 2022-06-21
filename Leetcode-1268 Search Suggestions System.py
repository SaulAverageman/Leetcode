class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        out=[]
        i=0
        
        for e in searchWord:
            nl=[]
            for p in products:
                if i< len(p) and p[i]==e:
                    nl.append(p)
            i+=1
            products=nl
            
            x=[nl[i] for i in range(min(3,len(nl)))]
            
            out.append(x)
        
        return out
