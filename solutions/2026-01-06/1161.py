from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Find the level with maximum sum in a binary tree using BFS.
        使用 BFS 找到二元樹中總和最大的層級。

        Args:
            root: The root node of the binary tree

        Returns:
            The smallest level x with maximum sum (1-indexed)
        """
        if not root:
            return 1

        max_sum = float('-inf')
        max_level = 1
        current_level = 1

        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Update max if current level has larger sum
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1

        return max_level


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: [1,7,0,7,-8,null,null]
    #       1
    #      / \
    #     7   0
    #    / \
    #   7  -8
    root1 = TreeNode(1)
    root1.left = TreeNode(7)
    root1.right = TreeNode(0)
    root1.left.left = TreeNode(7)
    root1.left.right = TreeNode(-8)
    assert sol.maxLevelSum(root1) == 2, "Test case 1 failed"
    print("Test case 1 passed: Expected 2, Got", sol.maxLevelSum(root1))

    # Example 2: [989,null,10250,98693,-89388,null,null,null,-32127]
    #           989
    #              \
    #             10250
    #             /    \
    #         98693   -89388
    #                     \
    #                   -32127
    root2 = TreeNode(989)
    root2.right = TreeNode(10250)
    root2.right.left = TreeNode(98693)
    root2.right.right = TreeNode(-89388)
    root2.right.right.right = TreeNode(-32127)
    assert sol.maxLevelSum(root2) == 2, "Test case 2 failed"
    print("Test case 2 passed: Expected 2, Got", sol.maxLevelSum(root2))

    print("\nAll test cases passed!")
