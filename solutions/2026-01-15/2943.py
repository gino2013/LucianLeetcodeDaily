from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        """
        Find the maximum area of a square-shaped hole in the grid.

        Args:
            n: Number of horizontal bars minus 2
            m: Number of vertical bars minus 2
            hBars: List of removable horizontal bars
            vBars: List of removable vertical bars

        Returns:
            Maximum area of a square-shaped hole
        """
        def find_max_consecutive(bars: List[int]) -> int:
            """Find the maximum length of consecutive bars."""
            if not bars:
                return 0
            bars.sort()
            max_len = 1
            current_len = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_len += 1
                    max_len = max(max_len, current_len)
                else:
                    current_len = 1
            return max_len

        max_hBars = find_max_consecutive(hBars)
        max_vBars = find_max_consecutive(vBars)

        # Side length is min of consecutive bars + 1
        size = min(max_hBars, max_vBars) + 1
        return size * size


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.maximizeSquareHoleArea(2, 1, [2,3], [2]) == 4
    print("Test 1 passed: n=2, m=1, hBars=[2,3], vBars=[2] -> 4")

    # Example 2
    assert sol.maximizeSquareHoleArea(1, 1, [2], [2]) == 4
    print("Test 2 passed: n=1, m=1, hBars=[2], vBars=[2] -> 4")

    # Example 3
    assert sol.maximizeSquareHoleArea(2, 3, [2,3], [2,4]) == 4
    print("Test 3 passed: n=2, m=3, hBars=[2,3], vBars=[2,4] -> 4")

    print("\nAll tests passed!")
