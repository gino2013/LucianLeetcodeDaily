from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        for diagonal in range(m + n - 1):
            if diagonal % 2 == 0:
                # Going up-right: start from bottom of diagonal
                row = min(diagonal, m - 1)
                col = diagonal - row
                
                while row >= 0 and col < n:
                    result.append(mat[row][col])
                    row -= 1
                    col += 1
            else:
                # Going down-left: start from top of diagonal
                col = min(diagonal, n - 1)
                row = diagonal - col
                
                while row < m and col >= 0:
                    result.append(mat[row][col])
                    row += 1
                    col -= 1
        
        return result