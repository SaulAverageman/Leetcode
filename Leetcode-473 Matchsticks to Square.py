class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        arr=[[set(),0]]
        t=sum(matchsticks)/4
        ll=[]
        for i in range(len(matchsticks)):
            e=matchsticks[i]
            l=len(arr)
            for ar in arr[:l]:
                if ar[1]>=t:
                    continue
                s=ar[0].copy()
                s.add(i)
                nar=[s,ar[1]+e]
                
                if nar[1]==t:
                    ll.append(s)
                else:
                    arr.append(nar)
        
        path=[set() for e in ll]
        for i in range(len(ll)):
            for j in range(i+1,len(ll)):
                if len(ll[i].intersection(ll[j]))==0:
                    path[i].add(j)
        self.out=0
        def go(i,s,d):
            if self.out==1:
                return
            if d==4:
                self.out=1
                return
            x=s.intersection(path[i])
            for e in x:
                go(e,x,d+1)
            
        for i in range(len(path)):
            go(i,path[i],1)
        return self.out
            
