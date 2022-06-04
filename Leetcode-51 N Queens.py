class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        out=[]
        col=[]
        
        def addstr(arr,out):
            nl=[]
            for e in arr:
                nl.append("".join(e))
            out.append(nl)
                
        def ck(j,col,i):
            for e in col:
                if j==e[1]:
                    return 1
                slope=abs(i-e[0])/abs(j-e[1])
                if slope==1 or slope==-1:
                    return 1
            return 0
            
        def go(board,i,col,n):
            if i==n:
                addstr(board,out)
                return
            for j in range(n):
                if ck(j,col,i):
                    continue
                board[i][j]="Q"
                col.append([i,j])
                go(board,i+1,col,n)
                board[i][j]="."
                col.pop(-1)
        go(board,0,col,n)
        
        return out
