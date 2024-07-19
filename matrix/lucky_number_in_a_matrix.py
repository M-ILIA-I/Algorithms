class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        """
        Problem description:

        Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

        A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
        """
        n = len(matrix)
        m = len(matrix[0])
        row_mins = [min(row) for row in matrix]

        col_maxs = [max(col) for col in zip(*matrix)]

        ln = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                    ln.append(matrix[i][j])
        return ln