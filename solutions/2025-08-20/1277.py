from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    total += dp[i][j]
        
        return total

def test_solution():
    sol = Solution()
    
    # Test case 1
    matrix1 = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]
    result1 = sol.countSquares(matrix1)
    print(f"Test 1: {result1} (expected: 15)")
    assert result1 == 15
    
    # Test case 2
    matrix2 = [
        [1,0,1],
        [1,1,0],
        [1,1,0]
    ]
    result2 = sol.countSquares(matrix2)
    print(f"Test 2: {result2} (expected: 7)")
    assert result2 == 7
    
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()