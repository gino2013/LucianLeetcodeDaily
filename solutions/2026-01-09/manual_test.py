from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        Find the smallest subtree containing all the deepest nodes.
        """
        def dfs(node):
            if not node:
                return (0, None)

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth + 1, node)

        return dfs(root)[1]


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a list of values (level-order traversal)."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# Test Example 1
print("Test Example 1:")
root1 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
solution = Solution()
result1 = solution.subtreeWithAllDeepest(root1)
print(f"Expected: 2, Got: {result1.val}")
assert result1.val == 2, f"Test 1 failed! Expected 2, got {result1.val}"
print("✓ Test 1 passed!\n")

# Test Example 2
print("Test Example 2:")
root2 = build_tree([1])
result2 = solution.subtreeWithAllDeepest(root2)
print(f"Expected: 1, Got: {result2.val}")
assert result2.val == 1, f"Test 2 failed! Expected 1, got {result2.val}"
print("✓ Test 2 passed!\n")

# Test Example 3
print("Test Example 3:")
root3 = build_tree([0, 1, 3, None, 2])
result3 = solution.subtreeWithAllDeepest(root3)
print(f"Expected: 2, Got: {result3.val}")
assert result3.val == 2, f"Test 3 failed! Expected 2, got {result3.val}"
print("✓ Test 3 passed!\n")

# Test balanced tree
print("Test Balanced Tree:")
root4 = build_tree([1, 2, 3])
result4 = solution.subtreeWithAllDeepest(root4)
print(f"Expected: 1, Got: {result4.val}")
assert result4.val == 1, f"Test 4 failed! Expected 1, got {result4.val}"
print("✓ Test 4 passed!\n")

print("All tests passed! ✓")
