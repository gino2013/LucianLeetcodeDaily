from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current: int) -> int:
            if node is None:
                return 0
            current = (current << 1) | node.val
            if node.left is None and node.right is None:
                return current
            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)


def build(vals: list, i: int = 0) -> Optional[TreeNode]:
    if i >= len(vals) or vals[i] is None:
        return None
    node = TreeNode(vals[i])
    node.left = build(vals, 2 * i + 1)
    node.right = build(vals, 2 * i + 2)
    return node


def test_solution():
    sol = Solution()

    # Example 1: [1,0,1,0,1,0,1] → 4+5+6+7 = 22
    root1 = build([1, 0, 1, 0, 1, 0, 1])
    assert sol.sumRootToLeaf(root1) == 22, "Test 1 failed"
    print("Test 1 passed: 22")

    # Example 2: [0] → 0
    root2 = build([0])
    assert sol.sumRootToLeaf(root2) == 0, "Test 2 failed"
    print("Test 2 passed: 0")

    # Single node with val 1 → 1
    root3 = build([1])
    assert sol.sumRootToLeaf(root3) == 1, "Test 3 failed"
    print("Test 3 passed: 1")

    # Path 1->1->0 = 6, 1->1->1 = 7 → 13
    root4 = build([1, None, 1, None, None, 0, 1])
    # build won't handle None correctly for non-complete trees; build manually
    r = TreeNode(1)
    r.right = TreeNode(1)
    r.right.left = TreeNode(0)
    r.right.right = TreeNode(1)
    assert sol.sumRootToLeaf(r) == 13, "Test 4 failed"
    print("Test 4 passed: 13")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
