from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        """
        Find the maximum area of a square field that can be formed by removing fences.

        Args:
            m: Field extends from row 1 to row m
            n: Field extends from column 1 to column n
            hFences: Horizontal fence positions (can be removed)
            vFences: Vertical fence positions (can be removed)

        Returns:
            Maximum square area modulo 10^9+7, or -1 if impossible
        """
        MOD = 10**9 + 7

        # Include boundaries (cannot be removed)
        h_positions = sorted([1, m] + hFences)
        v_positions = sorted([1, n] + vFences)

        # Generate all possible gaps for horizontal fences
        # A gap is the distance between any two fence positions
        # (we can remove all fences between them)
        h_gaps = set()
        for i in range(len(h_positions)):
            for j in range(i + 1, len(h_positions)):
                h_gaps.add(h_positions[j] - h_positions[i])

        # Generate all possible gaps for vertical fences
        v_gaps = set()
        for i in range(len(v_positions)):
            for j in range(i + 1, len(v_positions)):
                v_gaps.add(v_positions[j] - v_positions[i])

        # Find common gaps (squares require equal width and height)
        common_gaps = h_gaps & v_gaps

        if not common_gaps:
            return -1

        max_side = max(common_gaps)
        return (max_side * max_side) % MOD


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: m=4, n=3, hFences=[2,3], vFences=[2]
    # After removing h-fence at 2 and v-fence at 2, we get a 2x2 square
    result1 = sol.maximizeSquareArea(4, 3, [2, 3], [2])
    assert result1 == 4, f"Test 1 failed: expected 4, got {result1}"
    print("Test 1 passed: m=4, n=3, hFences=[2,3], vFences=[2] -> 4")

    # Example 2: m=6, n=7, hFences=[2], vFences=[4]
    # No common gaps exist for a square
    result2 = sol.maximizeSquareArea(6, 7, [2], [4])
    assert result2 == -1, f"Test 2 failed: expected -1, got {result2}"
    print("Test 2 passed: m=6, n=7, hFences=[2], vFences=[4] -> -1")

    # Additional test: Empty fences
    # h_positions = [1, 5], v_positions = [1, 4]
    # h_gaps = {4}, v_gaps = {3} -> no common
    result3 = sol.maximizeSquareArea(5, 4, [], [])
    assert result3 == -1, f"Test 3 failed: expected -1, got {result3}"
    print("Test 3 passed: m=5, n=4, hFences=[], vFences=[] -> -1")

    # Test: Square field with no internal fences
    result4 = sol.maximizeSquareArea(3, 3, [], [])
    assert result4 == 4, f"Test 4 failed: expected 4, got {result4}"
    print("Test 4 passed: m=3, n=3, hFences=[], vFences=[] -> 4")

    print("\nAll tests passed!")
