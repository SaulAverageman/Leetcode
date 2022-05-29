class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.out=[]
        arr=[["." for i in range(n)] for j in range(n)]
        def ck(arr,x):
            for e in arr:
                if e[0]==x[0]:
                    continue
                sl=(x[1]-e[1])/(x[0]-e[0])
                if sl in [1,-1,0]:
                    return 0
            return 1
        def go(arr,i,prev_arr,n):
            
            if i==n:
                
                self.out.append(["".join(e) for e in arr])
                return
            for j in range(n):
                 if ck(prev_arr,[i,j]):
                        arr[i][j]="Q"
                        prev_arr.append([i,j])
                        go(arr,i+1,prev_arr,n)
                        prev_arr.pop(-1)
                        arr[i][j]="."
        
        go(arr,0,[],n)
        return self.out