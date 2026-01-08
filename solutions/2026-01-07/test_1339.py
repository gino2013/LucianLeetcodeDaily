import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import from the problem file
import importlib.util
spec = importlib.util.spec_from_file_location("solution", os.path.join(os.path.dirname(__file__), "1339.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)

Solution = solution_module.Solution
TreeNode = solution_module.TreeNode

def test_example_1():
    """Test case 1: [1,2,3,4,5,6]"""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    solution = Solution()
    result = solution.maxProduct(root)
    expected = 110

    print(f"Test 1: Expected {expected}, Got {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✅ Test 1 passed!")

def test_example_2():
    """Test case 2: [1,null,2,3,4,null,null,5,6]"""
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(6)

    solution = Solution()
    result = solution.maxProduct(root)
    expected = 90

    print(f"Test 2: Expected {expected}, Got {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✅ Test 2 passed!")

def test_simple_case():
    """Test case 3: Simple tree [1,2,3]"""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    solution = Solution()
    result = solution.maxProduct(root)
    # Total sum = 6
    # Possible splits:
    # - Remove edge to left (2): 2 * 4 = 8
    # - Remove edge to right (3): 3 * 3 = 9
    expected = 9

    print(f"Test 3: Expected {expected}, Got {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✅ Test 3 passed!")

if __name__ == "__main__":
    print("Running tests for Problem 1339: Maximum Product of Splitted Binary Tree")
    print("=" * 70)

    test_example_1()
    print()
    test_example_2()
    print()
    test_simple_case()

    print()
    print("=" * 70)
    print("🎉 All tests passed!")
