class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out=[[0 for e in matrix] for e in matrix[0]]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                out[j][i]=matrix[i][j]
        return out
