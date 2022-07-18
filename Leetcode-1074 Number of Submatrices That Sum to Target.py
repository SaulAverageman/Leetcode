class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        out=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j!=0:
                    matrix[i][j]+=matrix[i][j-1]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i!=0:
                    matrix[i][j]+=matrix[i-1][j]
        
        for ii in range(len(matrix)):
            for i in range(ii,len(matrix)):
                di={0:1}
                for k in range(0,len(matrix[0])):
                    if ii==0:
                        a=0
                    else:
                        a=matrix[ii-1][k]
                    if matrix[i][k]-target-a in di:
                        #print("x",ii,i,k)
                        out+=di[matrix[i][k]-target-a]
                    if matrix[i][k]-a in di:
                        di[matrix[i][k]-a]+=1
                    else:
                        di[matrix[i][k]-a]=1
                            
        return out
