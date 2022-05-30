class Solution:
    def totalNQueens(self, n: int) -> int:
        self.out=0
        
        def ck(prev_arr,x):
            for e in prev_arr:
                if e[0]==x[0]:
                    return 0
                slope=(x[1]-e[1])/(x[0]-e[0])
                if slope in [1,-1,0]:
                    return 0
            return 1
        
        def go(i,prev_arr,n):
            if i==n:
                self.out+=1
                return
            for j in range(n):
                if ck(prev_arr,[i,j]):
                    prev_arr.append([i,j])
                    go(i+1,prev_arr,n)
                    prev_arr.pop(-1)
        go(0,[],n)
        return self.out