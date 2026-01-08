from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        # First pass: Calculate total sum of all nodes
        def calculate_total_sum(node):
            if not node:
                return 0
            return node.val + calculate_total_sum(node.left) + calculate_total_sum(node.right)

        total_sum = calculate_total_sum(root)
        max_product = 0

        # Second pass: For each subtree, calculate the product
        def calculate_subtree_sum(node):
            nonlocal max_product

            if not node:
                return 0

            # Calculate sum of current subtree
            left_sum = calculate_subtree_sum(node.left)
            right_sum = calculate_subtree_sum(node.right)
            subtree_sum = node.val + left_sum + right_sum

            # If we remove the edge above this subtree:
            # One part has sum = subtree_sum
            # Other part has sum = total_sum - subtree_sum
            product = subtree_sum * (total_sum - subtree_sum)
            max_product = max(max_product, product)

            return subtree_sum

        calculate_subtree_sum(root)

        return max_product % MOD
