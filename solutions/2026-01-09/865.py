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

        Strategy:
        - Use DFS to find depth and LCA for each subtree
        - For each node, return (depth, lca) where:
          * depth: maximum depth of nodes in this subtree
          * lca: root of smallest subtree with all deepest nodes
        - If left and right subtrees have equal depth, current node is the LCA
        - Otherwise, return the LCA from the deeper subtree

        Time Complexity: O(n) - visit each node once
        Space Complexity: O(h) - recursion stack, where h is tree height
        """
        def dfs(node):
            """
            Returns (depth, lca_node) tuple.

            Args:
                node: Current tree node

            Returns:
                Tuple of (depth, lca_node) where:
                - depth: depth of deepest node in this subtree
                - lca_node: LCA of all deepest nodes in this subtree
            """
            if not node:
                return (0, None)

            # Get depth and LCA from left and right subtrees
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            # If left subtree is deeper, answer is in left subtree
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            # If right subtree is deeper, answer is in right subtree
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            # If both subtrees have same depth, current node is the LCA
            else:
                return (left_depth + 1, node)

        return dfs(root)[1]
