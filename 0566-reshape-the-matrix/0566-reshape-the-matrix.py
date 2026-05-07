class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:
            return mat
        result=[[0]*c for i in range(r)]
        k=0
        for i in range(m):
            for j in range(n):
                result[k//c][k%c]=mat[i][j]
                k+=1
        return result
        