from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and ast < 0:
                if stack[-1] < abs(ast):
                    stack.pop()
                elif stack[-1] == abs(ast):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(ast)
        return stack


def test_solution():
    sol = Solution()

    # Test case 1
    result1 = sol.asteroidCollision([5, 10, -5])
    print(f"Test 1: {result1} (expected: [5, 10])")
    assert result1 == [5, 10]

    # Test case 2
    result2 = sol.asteroidCollision([8, -8])
    print(f"Test 2: {result2} (expected: [])")
    assert result2 == []

    # Test case 3
    result3 = sol.asteroidCollision([10, 2, -5])
    print(f"Test 3: {result3} (expected: [10])")
    assert result3 == [10]

    # Test case 4
    result4 = sol.asteroidCollision([3, 5, -6, 2, -1, 4])
    print(f"Test 4: {result4} (expected: [-6, 2, 4])")
    assert result4 == [-6, 2, 4]

    # Test case 5: all same direction
    result5 = sol.asteroidCollision([-2, -1, 1, 2])
    print(f"Test 5: {result5} (expected: [-2, -1, 1, 2])")
    assert result5 == [-2, -1, 1, 2]

    print("All tests passed!")

if __name__ == "__main__":
    test_solution()
