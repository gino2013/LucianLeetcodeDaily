from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Find boundaries of all 1's
        min_row, max_row = m, -1
        min_col, max_col = n, -1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        
        # Calculate area of bounding rectangle
        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    grid1 = [[0,1,0],[1,0,1]]
    result1 = sol.minimumArea(grid1)
    print(f"Test 1: {result1} (expected: 6)")
    assert result1 == 6
    
    # Test case 2  
    grid2 = [[1,0],[0,0]]
    result2 = sol.minimumArea(grid2)
    print(f"Test 2: {result2} (expected: 1)")
    assert result2 == 1
    
    # Additional test case
    grid3 = [[1,1,1],[0,1,0],[1,1,1]]
    result3 = sol.minimumArea(grid3)
    print(f"Test 3: {result3} (expected: 9)")
    assert result3 == 9
    
    print("All tests passed!")
