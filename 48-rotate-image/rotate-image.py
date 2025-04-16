class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Transpose
        #Iterate for i in range(len(matrix))
        for i in range(len(matrix)):
            #Iterate for j in range(i, len(matrix))
            for j in range(i, len(matrix)):
                #Switch values in matrix[i][j] with matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #Reverse
        #Iterate for row in matrix
        for row in matrix:
            #reverse each row to get vertical mirror image of the transposed matrix
            row.reverse()