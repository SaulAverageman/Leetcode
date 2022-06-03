class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr=matrix
        for i in range(1,len(self.arr)):
            self.arr[i][0]+=self.arr[i-1][0]
        
        for j in range(1,len(self.arr[0])):
            self.arr[0][j]+=self.arr[0][j-1]
        
        for i in range(1,len(self.arr)):
            for j in range(1,len(self.arr[0])):
                self.arr[i][j]+=self.arr[i-1][j]+self.arr[i][j-1]
                self.arr[i][j]-=self.arr[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total=self.arr[row2][col2]
        #print(col2,row2,total)
        if col1!=0:
            #print("-",row2,col1-1)
            total-=self.arr[row2][col1-1]
        
        if row1!=0:
            #print("-",row1-1,col2)
            total-=self.arr[row1-1][col2]
        
        if row1!=0 and col1!=0:
            #print("+",row1-1,col1-1)
            total+=self.arr[row1-1][col1-1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)