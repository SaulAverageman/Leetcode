class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x:len(x))
        def diff(a,b):
            ck=0
            i=0
            while i<len(a):
                if a[i]!=b[ck+i]:
                    ck+=1
                else:
                    i+=1
                if ck==2:
                    return 0
            return 1
        dil={}
        for i in range(len(words)):
            if len(words[i]) in dil:
                dil[len(words[i])].append([words[i],i])
            else:
                dil[len(words[i])]=[[words[i],i]]
        di={}
        for i in range(len(words)):
            di[i]=[]
            if len(words[i])+1 in dil:
                for e in dil[len(words[i])+1]:
                    if diff(words[i],e[0]):
                        di[i].append(e[1])        
        out=[0]
        vis=[0]*len(words)
        def dfs(i,c,vis,out):
            if vis[i]==1:
                return
            vis[i]=1
            if len(di[i])==0:
                out[0]=max(out[0],c)
            for j in di[i]:
                dfs(j,c+1,vis,out)
        for i in range(len(vis)):
            if vis[i]==0:
                dfs(i,1,vis,out)
        return out[0]
