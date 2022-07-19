class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out=[[] for i in range(numRows)]
        out[0].append(1)
        for i in range(1,numRows):
            for j in range(i+1):
                if j==0 or j==i:
                    out[i].append(1)
                else:
                    out[i].append(out[i-1][j]+out[i-1][j-1])
        return out
