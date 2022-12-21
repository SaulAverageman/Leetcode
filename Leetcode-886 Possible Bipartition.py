class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        di={(i+1):[] for i in range(n)}
        for e in dislikes:
            di[e[0]].append(e[1])
            di[e[1]].append(e[0])

        arr=[0]*(n+1)

        def go(node,color):
            if arr[node]==color:
                return 1

            arr[node]=color
            out=1
            for e in di[node]:
                if arr[e]==color:
                    return 0
                if arr[e]!=0:
                    continue
                out=out and go(e,-1*color)
            return out
        out=1
        for i in range(1,n+1):
            if arr[i]==0:
                out=out and go(i,1)
        return out
