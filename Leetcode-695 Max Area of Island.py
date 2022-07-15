class Solution:
    def maxAreaOfIsland(self, arr: List[List[int]]) -> int:
        self.out=0
        
        def go(i,j,arr):
            if i<0 or j<0 or i>=len(arr) or j>=len(arr[0]):
                return
            if arr[i][j]:
                self.area+=1
                arr[i][j]=0
                go(i-1,j,arr)
                go(i+1,j,arr)
                go(i,j-1,arr)
                go(i,j+1,arr)
                
        for i in range(len(arr)):
            for j in  range(len(arr[0])):
                if arr[i][j]:
                    self.area=0
                    go(i,j,arr)
                    self.out=max(self.out,self.area)
        return self.out
