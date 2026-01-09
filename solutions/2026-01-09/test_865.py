import pytest
from typing import Optional, List
import sys
sys.path.append('.')
from solutions.2026_01_09.865 import Solution, TreeNode


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a list of values (level-order traversal).
    None represents a null node.
    """
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


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Convert a binary tree to a list (level-order traversal).
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


class TestSolution:
    def test_example_1(self):
        """
        Test case 1: Tree with deepest nodes at depth 3
        Input: [3,5,1,6,2,0,8,null,null,7,4]
        Expected: Node with value 2
        """
        solution = Solution()
        root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        result = solution.subtreeWithAllDeepest(root)
        assert result.val == 2
        # The subtree rooted at 2 contains [2, 7, 4]
        assert result.left.val == 7
        assert result.right.val == 4

    def test_example_2(self):
        """
        Test case 2: Single node tree
        Input: [1]
        Expected: Node with value 1
        """
        solution = Solution()
        root = build_tree([1])
        result = solution.subtreeWithAllDeepest(root)
        assert result.val == 1

    def test_example_3(self):
        """
        Test case 3: Unbalanced tree with deepest node at depth 3
        Input: [0,1,3,null,2]
        Expected: Node with value 2
        """
        solution = Solution()
        root = build_tree([0, 1, 3, None, 2])
        result = solution.subtreeWithAllDeepest(root)
        assert result.val == 2

    def test_balanced_tree(self):
        """
        Test case 4: Perfectly balanced tree
        Input: [1,2,3]
        Expected: Node with value 1 (root is LCA of deepest nodes 2 and 3)
        """
        solution = Solution()
        root = build_tree([1, 2, 3])
        result = solution.subtreeWithAllDeepest(root)
        assert result.val == 1

    def test_left_heavy_tree(self):
        """
        Test case 5: Left-heavy tree
        Input: [1,2,null,3,null,4]
        Expected: Node with value 4 (deepest node)
        """
        solution = Solution()
        root = build_tree([1, 2, None, 3, None, 4])
        result = solution.subtreeWithAllDeepest(root)
        assert result.val == 4

    def test_right_heavy_tree(self):
        """
        Test case 6: Right-heavy tree
        Input: [1,null,2,null,3,null,4]
        Expected: Node with value 4 (deepest node)
        """
        solution = Solution()
        root = build_tree([1, None, 2, None, 3, None, 4])
        result = solution.subtreeWithAllDeepest(root)
        assert result.val == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
