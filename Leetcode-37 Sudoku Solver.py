class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def ck_row(arr,i,j,e):
            for k in range(9):
                if j!=k:
                    if arr[i][k]==e:
                        return 0
            return 1
        
        def ck_col(arr,i,j,e):
            for k in range(9):
                if k!=i:
                    if arr[k][j]==e:
                        return 0
            return 1
        
        def missing(arr,I,J):
            I=(I//3)*3
            J=(J//3)*3
            nset=set([str(e+1) for e in range(9)])
            for i in range(I,I+3):
                for j in range(J,J+3):
                    if arr[i][j]!=".":
                        nset.remove(arr[i][j])
            return list(nset)
        
        def go(arr,i,j):
            if i==9:
                return 1
            if j==9:
                return go(arr,i+1,0)
                
            if arr[i][j]!=".":
                return go(arr,i,j+1)
            
            miss_arr=missing(arr,i,j)
            
            for e in miss_arr:
                if ck_row(arr,i,j,e) and ck_col(arr,i,j,e):
                    arr[i][j]=e
                    if go(arr,i,j+1):
                        return 1
            arr[i][j]="."
            return 0
        
        go(board,0,0)