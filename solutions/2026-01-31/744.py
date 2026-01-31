from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        return letters[left % len(letters)]


def test_solution():
    sol = Solution()

    # Test case 1
    result1 = sol.nextGreatestLetter(["c", "f", "j"], "a")
    print(f"Test 1: {result1} (expected: c)")
    assert result1 == "c"

    # Test case 2
    result2 = sol.nextGreatestLetter(["c", "f", "j"], "c")
    print(f"Test 2: {result2} (expected: f)")
    assert result2 == "f"

    # Test case 3: target greater than all letters (wrap around)
    result3 = sol.nextGreatestLetter(["x", "x", "y", "y"], "z")
    print(f"Test 3: {result3} (expected: x)")
    assert result3 == "x"

    # Test case 4: target equal to last letter (wrap around)
    result4 = sol.nextGreatestLetter(["c", "f", "j"], "j")
    print(f"Test 4: {result4} (expected: c)")
    assert result4 == "c"

    # Test case 5: target between letters
    result5 = sol.nextGreatestLetter(["c", "f", "j"], "d")
    print(f"Test 5: {result5} (expected: f)")
    assert result5 == "f"

    print("All tests passed!")

if __name__ == "__main__":
    test_solution()
