class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        di={}
        arr.sort()
        
        for e in arr:
            di[e]=1
            for k in di.keys():
                if e/k in di:
                    if k!=e/k:
                        di[e]+=(di[k]*di[e/k])
                    else:
                        di[e]+=(di[k]*di[e/k])
        return sum(di.values())%1000000007
