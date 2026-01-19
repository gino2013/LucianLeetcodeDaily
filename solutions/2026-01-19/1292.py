from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Build 2D prefix sum array
        # prefix[i][j] = sum of submatrix from (0,0) to (i-1, j-1)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (mat[i-1][j-1] + prefix[i-1][j] +
                               prefix[i][j-1] - prefix[i-1][j-1])

        def get_sum(r1, c1, r2, c2):
            """Get sum of submatrix from (r1,c1) to (r2,c2) inclusive."""
            return (prefix[r2+1][c2+1] - prefix[r1][c2+1] -
                   prefix[r2+1][c1] + prefix[r1][c1])

        def can_find_square(k):
            """Check if there exists a square of side k with sum <= threshold."""
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if get_sum(i, j, i + k - 1, j + k - 1) <= threshold:
                        return True
            return False

        # Binary search on the side length
        left, right = 0, min(m, n)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if mid == 0 or can_find_square(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


def test_solution():
    sol = Solution()

    # Test case 1
    mat1 = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
    result1 = sol.maxSideLength(mat1, 4)
    print(f"Test 1: {result1} (expected: 2)")
    assert result1 == 2

    # Test case 2
    mat2 = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
    result2 = sol.maxSideLength(mat2, 1)
    print(f"Test 2: {result2} (expected: 0)")
    assert result2 == 0

    # Test case 3: single element within threshold
    mat3 = [[5]]
    result3 = sol.maxSideLength(mat3, 5)
    print(f"Test 3: {result3} (expected: 1)")
    assert result3 == 1

    # Test case 4: single element above threshold
    mat4 = [[5]]
    result4 = sol.maxSideLength(mat4, 4)
    print(f"Test 4: {result4} (expected: 0)")
    assert result4 == 0

    print("All tests passed!")

if __name__ == "__main__":
    test_solution()
