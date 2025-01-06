class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import copy
        copy_matrix = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if copy_matrix[i][j] == 0:
                    for k in range(len(copy_matrix)):
                        matrix[k][j] = 0
                    for l in range(len(copy_matrix[0])):
                        matrix[i][l] = 0
        